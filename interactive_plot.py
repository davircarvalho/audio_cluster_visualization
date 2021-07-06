import matplotlib.pyplot as plt
import numpy as np 
from operator import itemgetter
import sounddevice as sd

class interactive_plot:
    def __init__(self, x, y, data, sr):
        self.x = x              # List of x coordinates of clustered samples
        self.y = y              # List of y coordinates of clustered samples
        self.audio_table = np.transpose(data) # Array with audio samples: inputsize = [number_of_data_samples x audio_length]
        self.sr = sr

        # Play/stop plot specs 
        self.currently_playing = [x[0], y[0]] # initialize variable 
        self.color_play = 'r' # red
        self.color_idle = 'k' # black

        self.fig = plt.figure(figsize=(8,8))
        self.cidpress = self.fig.canvas.mpl_connect(
            'button_press_event', self.on_click)
        self.cidkey = self.fig.canvas.mpl_connect(
            'key_press_event', self.on_key)


    def PlotClusters(self):
        plt.scatter(self.x, self.y, c=self.color_idle)
        plt.title('click on the point to listen, press a key to stop it')
        plt.axis('off')
        plt.show()

    ### CALLBACKS ###
    def on_click(self, event):
        """Check whether mouse is over us; if so, store some data."""
        x_data = event.xdata
        y_data = event.ydata
        
        # Change color (make sure there's always only one point in red)
        plt.scatter(self.currently_playing[0], self.currently_playing[1], c=self.color_idle)
        plt.show()

        # find index that matches the clicked position and play the corresponding sound
        point_dist = np.sqrt((self.x - x_data)**2 + (self.y - y_data)**2 ) # distance between ploted points and click location
        idx_audio = min(enumerate(point_dist), key=itemgetter(1))[0]       # find the closest point to click position
        self.currently_playing = [self.x[idx_audio], self.y[idx_audio]]

        # Play the audio file 
        data = self.audio_table[:,idx_audio]
        self.playing_audio = sd.play(data, self.sr)

        # Change color 
        plt.scatter(self.currently_playing[0], self.currently_playing[1], c=self.color_play)
        plt.show()

    def on_key(self, event):
        sd.stop(self.playing_audio)
        plt.scatter(self.currently_playing[0], self.currently_playing[1], c=self.color_idle)
        plt.show()

    def disconnect(self):
        """Disconnect all callbacks."""
        self.fig.canvas.mpl_disconnect(self.cidpress)
        # self.fig.canvas.mpl_disconnect(self.cidrelease)
        # self.fig.canvas.mpl_disconnect(self.cidmotion)

