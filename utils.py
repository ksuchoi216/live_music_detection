from tqdm import tqdm
import os
import pandas as pd

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import re

def spotify_api(cfg):
    os.environ['SPOTIPY_CLIENT_ID'] = cfg.SPOTIPY_CLIENT_ID
    os.environ['SPOTIPY_CLIENT_SECRET'] = cfg.SPOTIPY_CLIENT_SECRET
    return spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def create_data(cfg, sp, df):   
    track_ids = df['id'][:cfg.n_samples]
    audio_feats = pd.DataFrame(columns=cfg.data_cols)
    for i, track_id in enumerate(tqdm(track_ids)):
        track = sp.track(track_id)
        audio_feat = sp.audio_features(track_id)[0]
        audio_feat['name'] = track['name']
        audio_feat['sample_30s'] = track['preview_url']
            
        # if full_data == True:
        #     artists = []
        #     for i in range(len(track['artists'])):
        #         artists.append(track['artists'][i]['name'])
        #     audio_feat['artists'] = artists
        #     audio_feat['popularity'] = track['popularity']
        #     audio_feat['release_date'] = track['album']['release_date']
        
        audio_feats=audio_feats.append(audio_feat, ignore_index=True)
        
    return audio_feats

def write_df(df, cfg):
    #create csv file
    new_filename = cfg.new_filename
    filepath_save = cfg.filepath_save
    path = filepath_save + new_filename
    df.to_csv(path)
    print('file created at ',path)
    
    
def normalisation(df, opt_min_max=False):
    if opt_min_max == False:
        return (df-df.mean())/df.std()
    elif opt_min_max == True:
        return (df-df.min())/(df.max()-df.min())
    
def plot(df, cols=5, rows=2):
    matplotlib.rcParams['figure.figsize'] = [20, 8]
    cols = cols
    rows = rows
    fig, axes = plt.subplots(rows,cols, sharey=True)
    
    for i, item in enumerate(df):
        col = i%cols
        row = i//cols
        
        sns.regplot(ax=axes[row,col], data=df, x='liveness', y=item, scatter_kws={"color": "black"}, line_kws={"color": "red"})
    
    plt.show()



def detect_live_in_name(df):

    df['live'] = 0
    
    for i, name in enumerate(df['name']):
        find_tokens = re.findall(r'([-/] [Ll]ive|\([Ll]ive\))', name)
        if find_tokens:
            df['live'][i] = 1
            
    return df

