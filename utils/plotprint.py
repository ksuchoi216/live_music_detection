from tqdm import tqdm
import os
import pandas as pd

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import re

def plot(df, x='liveness', plot_type = 'boxplot', color = 'blue'):
    matplotlib.rcParams['figure.figsize'] = [10, 8]
    sns.set_theme(style='whitegrid')
    
    if plot_type == 'boxplot':    
        ax = sns.boxplot(data=df, x=x, color = color)
        # ax = sns.swarmplot(data=df, x=x, color=".25")
        
    if plot_type == 'histplot':
        ax = sns.histplot(data=df, x=x, color = color)
    
def multi_plot(df, col_name='liveness', cols=6, rows=2):
    matplotlib.rcParams['figure.figsize'] = [20, 8]
    cols = cols
    rows = rows
    fig, axes = plt.subplots(rows,cols, sharey=True)
    
    for i, item in enumerate(df):
        print(i," ...")
        col = i%cols
        row = i//cols
        
        sns.regplot(ax=axes[row,col], data=df, x=col_name, y=item, scatter_kws={"color": "black"}, line_kws={"color": "red"})
    
    plt.show()
    

def fprint(item, value):
    print('{:20}: {} '.format(item, value))

def print_keys(keys):
    for i, key in enumerate(keys):
        print("{} : {}".format(i, key))
        
def df_print_info(df, item='liveness'):
    data=df
    print('[{:14}]{}'.format('max/min/mean','-'*40))
    print('{:14}: {} '.format(item+' max', data[item].max()))
    print('{:14}: {} '.format(item+' min', data[item].min()))
    print('{:14}: {} '.format(item+' mean', data[item].mean()))
    print('[{:14}]{}'.format('quantile','-'*40))
    print(data[item].quantile([0.05, 0.25, 0.5, 0.75, 0.95]))