import pandas as pd
import numpy as np

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
