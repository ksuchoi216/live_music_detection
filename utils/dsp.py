import matplotlib.pyplot as plt #visualisation

#audio analysis library
import librosa
import librosa.display

def show_freq_spec(path, log_scale=False):
    path = path
    t, sr = librosa.load(path) #audio time series and sampling rate
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(t, sr=sr) #show wave signal in the figure.

    F = librosa.stft(t)
    Fdb = librosa.amplitude_to_db(abs(F))
    plt.figure(figsize=(14, 5))

    if log_scale == True:
        librosa.display.specshow(Fdb, sr=sr, x_axis='time', y_axis='log')
        plt.colorbar()
        plt.show()
    else:
        librosa.display.specshow(Fdb, sr=sr, x_axis='time', y_axis='hz')
        plt.colorbar()
        plt.show()