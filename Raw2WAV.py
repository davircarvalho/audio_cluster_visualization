# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:26:40 2021

@author: rdavi

AEmotion from raw to wav
"""

# %% Imports
import sys 
sys.path.append('..')
import os
import librosa
import soundfile as sf 


# %% Convert from whatever format to WAV
path_in = 'AUDIOS'
path_out = os.getcwd() + os.path.sep + 'wav_data' 
if not os.path.exists(path_out):
    os.makedirs(path_out)
for subdir, dirs, files in os.walk(path_in):
    for file in files:
        data, Fs = librosa.load(subdir + os.path.sep + file, sr=None)
        file = path_out + os.path.sep + file.split('.')[0] + '.wav'
        sf.write(file, data, samplerate=Fs, format='WAV')   



# %%
