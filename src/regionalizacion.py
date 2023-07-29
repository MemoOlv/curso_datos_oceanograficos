from ocean_data import read_netcdf_from_path, AEE
from glob import glob
import numpy as np


netcdf_files = glob("datos/sst_gm/SST*.nc")

variable_name = "analysed_sst"

temperatures = []
flatten_temperatures = []
for i in range(0, len(netcdf_files)):
    netcdf_data = read_netcdf_from_path(netcdf_files[i])
    variable = netcdf_data[variable_name][0][:, :]
    temperatures.append(variable)
    del variable

    temperature = netcdf_data[variable_name][0]
    flatten_temperature = temperature.T.reshape(-1)
    flatten_temperatures.append(flatten_temperature)


M_sin_estandarizar = flatten_temperatures
print(np.nanmin(M_sin_estandarizar))

M_estandarizada = [AEE(i) for i in M_sin_estandarizar]
print("Tamaño: ", np.shape(M_estandarizada))
print("Prueba de estandarización (media): ", np.nanmean(M_estandarizada[0]))
print("Prueba de estandarización (std): ", np.std(M_estandarizada[0]))


M_cov = np.cov(M_estandarizada)
print("Cov matriz:", M_cov)

eigenvalues, eigenvectors = np.linalg.eig(M_cov)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

feo = M_cov * (-1*eigenvectors)

feo_1 = feo[0]
print("feo1: ", feo_1)
