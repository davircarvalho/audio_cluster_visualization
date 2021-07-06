# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 2021

@author: rdavi

AEmotion normalization, filtering and de-noising
"""

# %% Imports
import sys 
sys.path.append('..')
import os
import librosa
import soundfile as sf
import numpy as np
from scipy import signal


# %% Define high-pass filter
def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y


# %% Convert from whatever format to WAV
path_in = 'wav_data'
path_out = os.getcwd() + os.path.sep + 'processed_data' 
if not os.path.exists(path_out):
    os.makedirs(path_out)
for subdir, dirs, files in os.walk(path_in):
    for file in files:
        data, Fs = librosa.load(subdir + os.path.sep + file, sr=44100)       

        # High-pass filter
        data = butter_highpass_filter(data, cutoff=150, fs=Fs, order=5)
        
        # Normalization 
        data = np.divide(data, np.max(np.absolute(data))) * 0.97

        # Write data
        file = path_out + os.path.sep + file.split('.')[0] + '.wav'
        sf.write(file, data, samplerate=Fs, format='WAV')   


# %%
