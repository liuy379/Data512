import pandas as pd
import numpy as np

def create_hour_bin(x):
    if (x >= 0) & (x < 4):
        out = '0_4'
    elif (x >= 4) & (x < 8):
        out = '4_8'
    elif (x >= 8) & (x < 12):
        out = '8_12'
    elif (x >= 12) & (x < 16):
        out = '12_16'
    elif (x >= 16) & (x < 20):
        out = '16_20'
    else:
        out = '20_24'
    return out

def group_priority(x):
    if x == 3 or x == 4:
        x = '3 & 4'
    elif x >= 5:
        x = '5+'
    return x