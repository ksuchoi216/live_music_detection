#file
filepath_load = '/Users/KC/My Drive/soundmouse/data/task100k.csv'
filepath_save = '/Users/KC/My Drive/soundmouse/data/'
filepath_mp3 = '/Users/KC/My Drive/soundmouse/mp3/'

#spotify api
SPOTIPY_CLIENT_ID = 'f0967aa1c7064a36856282c85b3644a4'
SPOTIPY_CLIENT_SECRET = 'bc71b4a60b154c4687a702d115d8dfba'

#sample
n_samples = 10000 #select the number of samples

#data
audio_feat_cols = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 
             'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 
             'analysis_url', 'duration_ms', 'time_signature']

normalised_cols= ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms',
       'time_signature']

selected_cols = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
    'duration_ms','time_signature', 'live', 'outlier']

drop_cols = ['outlier','live']
label_col = 'outlier'

#deep learning model
#image save filepath
img_save_path = '/Volumes/ehd/prog/data/soundmouse/img_sample30s/'
np_save_path = '/Users/KC/My Drive/soundmouse/data/'

#model
model = {'l1':[13,26],
         'l2':[26,13],
         'l3':[13,6],
         'l4':[6,1],
         'dropout':0.2}

#execute
epochs = 10
interval = 1000
batch_size = 16


