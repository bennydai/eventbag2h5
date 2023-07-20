import pandas as pd
import numpy as np
import time

# Directory
directory = "/root/data/"

# h5 Filename
h5_filename = "shapes_6dof.h5"

# start time for h5 timing
start = time.time()

# Read event data from h5
df = pd.read_hdf(directory + h5_filename, "events")

# end time
end = time.time()

print("Time taken to parse in h5", (end - start))

# Some example code for splitting into np arrays
x = df['x'].to_numpy()
y = df['y'].to_numpy()
t = df['t'].to_numpy()

print("Number of data points", len(x), len(y), len(t))
