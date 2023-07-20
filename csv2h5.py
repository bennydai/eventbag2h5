import pandas as pd
import numpy as np
import time

# Directory
directory = "/root/data/"

# CSV filename
csv_filename = "events.txt"

# Output h5 filename
output_h5 = "shapes_6dof.h5"

# Start time for csv timing
start = time.time()

# Construct dataframe
df = pd.read_csv(directory + csv_filename,
    names=['t', 'x', 'y', 'p'], sep='\s+')

# Finished parsing
end = time.time()

# Convert to h5
df.to_hdf(directory + output_h5, key="events")

print("Time taken to parse in csv", (end - start))
