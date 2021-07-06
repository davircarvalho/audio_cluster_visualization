'''
Clustering audios dataset CM via TSNE   
'''


# %% Import Libs
import os 
import librosa
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.manifold import TSNE


# %% Load audios
def load_and_preprocess(path_in):
    # path_in = 'processed_data' 
    sr = 44100
    audio_length = 60 # segundos
    N = sr*audio_length
    Nfile = 55 
    data = np.zeros(shape=(N, Nfile))
    cont=0
    for subdir, dirs, files in os.walk(path_in):
        for file in files:
            audio, Fs = librosa.load(subdir + os.path.sep + file, sr=None) 
            ln_audio = len(audio)
            if ln_audio > N:
                data[:,cont] = audio[:N,]
            else:
                data[:ln_audio,cont] = audio
            cont +=1

    data = np.transpose(data)
    return data, sr

# %% Learning 
def tsne_cluster(data):
    model = TSNE(learning_rate=50, random_state=0, n_components=2, perplexity=51, n_iter=5000)
    transformed =model.fit_transform(data)
    xs = transformed[:,0]
    ys = transformed[:,1]
    return xs, ys

# %% View results
# xs = transformed[:,0]
# ys = transformed[:,1]
# plt.scatter(xs, ys)
# plt.show()

# %%
