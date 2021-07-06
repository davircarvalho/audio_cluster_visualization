'''
    Generate clusters via tsne and generate interactive plots
'''
# %% 
from clustering import load_and_preprocess, tsne_cluster
from interactive_plot import interactive_plot
import numpy as np 

def process():
    # Load and generate clusters
    dataset_path = 'processed_data' 
    data, sr = load_and_preprocess(dataset_path)
    x, y = tsne_cluster(data)
    
    # Interactive plot    
    iplt = interactive_plot(x, y, data, sr)
    iplt.PlotClusters()
    

if __name__ == "__main__":
    process()
