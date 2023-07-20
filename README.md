# eventbag2h5
Code is written by myself to indicate a small example on how to extract ```dvs/events``` from a rosbag. To save time reloading events all the time, the usage of the ```hdf5``` format to load event data is much more efficient that parsing in csv or the rosbag itself.

The code only includes extraction of the event topic from the ```DAVIS``` line of event cameras. The extraction code is written in Python, but requires some C++ packages/libraries to be installed in order for it to work.

## C++ Requirements
- libcaer-dev
- ROS
- rpg_dvs_ros

Refer to [rpg_dvs_ros](https://github.com/uzh-rpg/rpg_dvs_ros) for installation guide for the above C++ requirements.

## Python Requirements
- pandas
- numpy
- tables
- h5py

To install the above, ```Python3``` is required. All libraries mentioned above are now deprecated in ```Python2```. To install any of the above Python packages, the usage of the Python package installer pip will be sufficient.

As for example:
```bash
pip3 install pandas
```

to install the ```pandas``` package.

## Code usage
For ```bag2csv.py``` the parameters on top of the script should contain the path of your directory of where the rosbag and where the csv file be written to. We retain the ```sep=" "``` to be in line with some other datasets that are online as they also provide csv file formats.

For ```csv2h5.py``` the parameters on top of the script should contain the path of your directory of where your output csv file resides and what your h5 output name would be.

I have written a small example on how to parse in ```hdf5``` files using the ```pandas``` library as it has a very powerful API for large datasets.

All these files are also timed in how long they get taken to be parsed 100%.

## Tested ROS environments
This code has been tested against the following ROS distributions using Docker Containers:
- ROS Melodic (Ubuntu 18.04)
- ROS Noetic (Ubuntu 20.04)

## Tested version history
- ```python3==3.8.10```
- ```pandas==2.0.3```
- ```numpy==1.24.4```
- ```tables==3.8.0```
- ```h5py==3.9.0```

## Some warnings for larger files such as images
If you do decide to use ```hdf5``` in the future, I would strongly suggest you to not index the actual images, but rather where it resides in the ```hdf5```.

You will also notice that the event-only ```.h5``` file is much larger than the ```rosbag``` that you began with, even though it contains only event data. This is the trade-off that occurs as ```.h5``` is essentially a binary format.
