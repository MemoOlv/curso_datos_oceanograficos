from ocean_data import read_netcdf_from_path, AEE
from glob import glob
from functools import reduce
import numpy as np


netcdf_files = glob("datos/sst_gm/SST*.nc")

variable_name = "analysed_sst"

temperatures = []
flatten_temperatures = []
for i in range(0, len(netcdf_files)):
    netcdf_data = read_netcdf_from_path(netcdf_files[i])
    variable = netcdf_data[variable_name][0][:,:]
    temperatures.append(variable)
    del variable

    temperature = netcdf_data[variable_name][0]
    temp_dim = reduce((lambda x, y: x * y), temperature.shape)
    flatten_temperature = temperature.reshape(temp_dim)
    flatten_temperatures.append(flatten_temperature)


M_sin_estandarizar = np.array(flatten_temperatures)
print(M_sin_estandarizar)

M_estandarizada = [AEE(i) for i in M_sin_estandarizar ]
print("Prueba de estandarización (media): ", np.nanmean(M_estandarizada[0]))
print("Prueba de estandarización (std): ", np.std(M_estandarizada[0]))


