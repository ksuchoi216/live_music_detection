from tqdm import tqdm
import os
import pandas as pd

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import re


def write_df(cfg, df, filename):
    #create csv file
    filepath_save = cfg.filepath_save
    path = filepath_save + filename
    df.to_csv(path, index=False)
    print(filename,' file created at ',path)
    
    
def normalisation(df, opt_min_max=False):
    if opt_min_max == False:
        return (df-df.mean())/df.std()
    elif opt_min_max == True:
        return (df-df.min())/(df.max()-df.min())
    



def detect_live_in_name(df):
    df['live'] = 0
    
    for i, name in enumerate(df['name']):
        find_tokens = re.findall(r'([-/] [Ll]ive|\([Ll]ive\))', name)
        if find_tokens:
            df['live'][i] = 1
            
    return df
