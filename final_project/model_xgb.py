import utils
import math
import pandas as pd
import numpy as np
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar

def create_hour_bin(x):
    if (x >= 0) & (x < 4):
        out = 'call_hour_0_4'
    elif (x >= 4) & (x < 8):
        out = 'call_hour_4_8'
    elif (x >= 8) & (x < 12):
        out = 'call_hour_8_12'
    elif (x >= 12) & (x < 16):
        out = 'call_hour_12_16'
    elif (x >= 16) & (x < 20):
        out = 'call_hour_16_20'
    else:
        out = 'call_hour_20_24'
    return out

ds = pd.read_csv('/home/ubuntu/data/call_data_filtered.csv')

ds['Original Time Queued'] = pd.to_datetime(ds['Original Time Queued'])

# Features

ds['Call_Hour'] = ds['Original Time Queued'].dt.hour
ds['Call_Weekday'] = ds['Original Time Queued'].dt.weekday

ds['Call_Hour_Bin'] = ds['Call_Hour'].apply(utils.create_hour_bin)

# extract holiday info
cal = calendar()
holidays = cal.holidays(start=ds['Original Time Queued'].min(), end=ds['Original Time Queued'].max())
ds['is_Holiday'] = ds['Original Time Queued'].dt.date.isin(pd.Series(holidays).dt.date).astype(int)

# encoding
ds = ds[['Call Type','Priority','Precinct','Sector','response_time','Call_Weekday','Call_Hour_Bin','is_Holiday']]

ds = pd.get_dummies(ds,
               columns=['Call Type','Priority','Precinct','Sector','Call_Weekday','Call_Hour_Bin'],
               prefix=['Call Type','Priority','Precinct','Sector','Call_Weekday','Call_Hour_Bin'])

# Train and Validation

from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(ds.drop(columns=['response_time']),
                                                  ds['response_time'],
                                                  test_size=0.2,
                                                  random_state=10)

# Random Forest

# from sklearn.ensemble import RandomForestRegressor
#
# forest_reg = RandomForestRegressor(n_estimators=20, random_state=10, criterion='rmse',
#                                   min_samples_leaf=10)
# forest_reg.fit(X_train, y_train)
#
# pred_forest = forest_reg.predict(X_val)
#
# math.sqrt(sum((y_val - pred_forest)**2))

# param_grid = [{'max_depth': [10, 20, 30],
#                'min_samples_leaf': [1, 2, 4],
#                'min_samples_split': [2, 5, 10],
#                'n_estimators': [100, 200, 400]}]

# forest_clf = RandomForestRegressor(n_estimators=20, random_state=10)

# grid_search_full = GridSearchCV(forest_clf, param_grid, cv=3, verbose=3, n_jobs=-1)
# grid_search_full.fit(X, y)

# Xgboost

import xgboost as xgb

dtrain = xgb.DMatrix(X_train, label=y_train)
dval = xgb.DMatrix(X_val, label=y_val)

param = {
    'objective': 'reg:squarederror',
    'eva_metric': 'rmse',
    'eta': 0.03,
    'subsample': 0.8,
    'colsample': 0.8,
    'max_depth': 6
}

num_round = 50

# specify validations set to watch performance
watchlist = [(dtrain, 'train'), (dval, 'eval')]
print('Training starts...')
bst = xgb.train(param,
                dtrain,
                num_round,
                watchlist,
                verbose=1,
                early_stopping_rounds=10)

print('Saving model')
bst.save('model')
