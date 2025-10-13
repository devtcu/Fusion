# nuclei_sampler.py
import pandas as pd
import numpy as np

def load_or_sample_coordinates(n_points=200, from_csv=None):
    if from_csv:
        coords = pd.read_csv('../nuclei-coordinates.csv').values
    else:
        coords = np.random.rand(n_points, 2) * 1000  # synthetic tissue section
    return coords
