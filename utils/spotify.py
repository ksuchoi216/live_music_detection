from tqdm import tqdm
import os
import pandas as pd

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import re

from .utils import write_df

import os.path
from tqdm import tqdm

def spotify_api(cfg):
    os.environ['SPOTIPY_CLIENT_ID'] = cfg.SPOTIPY_CLIENT_ID
    os.environ['SPOTIPY_CLIENT_SECRET'] = cfg.SPOTIPY_CLIENT_SECRET
    # os.environ['PIP_DEFAULT_TIMEOUT'] = 1000
    return spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())



def create_feat_file(cfg, df, sp, filename='audio.csv', return_value = False):
    print(cfg.audio_feat_cols)
    n_samples = cfg.n_samples
    track_ids = df['id']
    audio_feats = df
    update_feats = pd.DataFrame(columns=cfg.audio_feat_cols)
    
    num_tracks=track_ids.shape[0]//100+1
    for i in tqdm(range(num_tracks)):
        start=100*i
        end=(i+1)*100 - 1
        # print('This loop for ',start,' to ', end)
        audio_feat = sp.audio_features(track_ids[start:end])
        update_feats = update_feats.append(audio_feat, ignore_index=True)
        
        # for key, value in audio_feat.items():
            # audio_feats[key][i] = value
            
    write_df(cfg, update_feats, filename)
    if return_value == True:
        return update_feats

# def create_data_file(cfg, df, sp):
    
#     n_samples = cfg.n_samples
#     track_ids = df['id']
#     audio_feats = df

#     for col in cfg.add_cols:
#         audio_feats[col] = ''
    
#     for i, track_id in enumerate(tqdm(track_ids)):
#         track = sp.track(track_id)
#         audio_feat = sp.audio_features(track_id)[0]
#         for key, value in audio_feat.items():
#             audio_feats[key][i] = value
#         audio_feats['preview_url'] = track['preview_url']
        
#         if i % n_samples == (n_samples-1):
#             start = i//n_samples*n_samples
#             end = i
#             filename = 'audio_feats_'+str(start)+'_to_'+str(end)+'.csv'
#             save_data = audio_feats.iloc[start:end,:]
#             write_df(cfg, save_data, filename)