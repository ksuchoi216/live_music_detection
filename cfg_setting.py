#file
filepath_load = '/Users/KC/My Drive/soundmouse/data/task100k.csv'
filepath_save = '/Users/KC/My Drive/soundmouse/data/'
new_filename = 'audio_feats.csv'

#spotify api
SPOTIPY_CLIENT_ID = 'f0967aa1c7064a36856282c85b3644a4'
SPOTIPY_CLIENT_SECRET = 'bc71b4a60b154c4687a702d115d8dfba'

#sample
n_samples = 1000 #select the number of samples

#data
data_cols = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 
        'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 
        'analysis_url', 'duration_ms', 'time_signature','popularity','release_date','artists', 'sample_30s']

selected_cols = ['name', 'danceability', 'energy', 'key', 'loudness','speechiness', 'acousticness', 
                 'instrumentalness', 'liveness', 'valence', 'tempo']

drop_cols = ['name', 'liveness']