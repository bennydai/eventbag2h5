import numpy as np
import rosbag
import time

# Directory
directory = "/root/data/"

# Rosbag name
bag_filename = "shapes_6dof.bag"

# Output csv filename for event
output_csv_filename = "events.txt"

# Read bag file
bag = rosbag.Bag(directory + bag_filename)

# Timing event loop
start = time.time()

# Seperator
sep = " "

# Open output csv file
eventFile = open(directory + output_csv_filename, "w")

# Writing events
for topic, msg, t in bag.read_messages(topics=['/dvs/events']):
    for event in msg.events:
        buffer = ((str(event.ts.secs + (event.ts.nsecs * 1e-9)) + sep +
            str(event.x) + sep + str(event.y) + sep +
            str(int(event.polarity)) + "\n"))
        eventFile.write(buffer)

# Calculate time for end of loop
end = time.time()

# Close file
eventFile.close()

print("Time taken to loop events with rosbag api", (end - start))
