```python
audio_fts.isna().sum() # check null values

from sklearn import preprocessing
import numpy as np

dft = pd.DataFrame(np.array([[1, 3, 3], [1, 5, 6], [4, 5, 9]]),
                   columns=['a', 'b', 'c'])

dft
# print(dft.sum()/dft.shape[0])
# print(dft.max())
# print(dft.min())
# print(dft.max()-dft.min())
x = dft.values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
# x_scaled2 = (dft-dft.min())/(dft.max()-dft.min())
print(x_scaled)

x_scaled = normalisation(dft, opt_min_max=True)
print(x_scaled)

```python
res_keys = list(res[0].keys())

print('\naudio feature keys: ', res_keys)
print(type(res_keys))

print('\ntrack preview_url(30s sample): ',track['preview_url'])

print('-'*130)

# print('\ntrack name: ', track)

print('\ntrack name: ', track['name'])

artists = []
for i in range(len(track['artists'])):
    artists.append(track['artists'][i]['name'])
print('artists: ',artists)
# print('\ntrack artists: ', track['artists'][0]['name'])
# print('\ntrack artists: ', track['artists'][1]['name'])

print('\ntrack popularity: ', track['popularity'])

# print('\ntrack release date: ', track['artists']['release_date'])

print('\ntrack release_date: ',track['album']['release_date'])  

# for key, value in track.items():
#     print('{} | {}'.format(key,value))
#     for v in value:
#         print('{}||{}'.format(key, v))
```