from ocean_data import read_netcdf_from_path
from glob import glob
import matplotlib.pyplot as plt
from functools import reduce
import numpy as np

netcdf_files = glob("tests/data/*.nc")

temperatures = []
for i in range(3):
    netcdf_data = read_netcdf_from_path(netcdf_files[i])
    temperature = netcdf_data["analysed_sst"][0]
    temp_dim = reduce((lambda x, y: x * y), temperature.shape)
    flatten_temperature = temperature.reshape(temp_dim)
    temperatures.append(flatten_temperature)


f = plt.figure()
plt.hist(temperatures)
filename = f"temperature_histogram.png"
f.savefig(filename)
