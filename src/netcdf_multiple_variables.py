from ocean_data import read_netcdf_from_path, get_latitude_and_longitude, AEE

import matplotlib.pyplot as plt
import numpy as np


netcdf_file = "tests/data/4903185_prof.nc"

netcdf_data = read_netcdf_from_path(netcdf_file)
longitude, latitude = get_latitude_and_longitude(netcdf_data)

variable_name_x = "TEMP"
variable_name_y = "PSAL"
temp = netcdf_data["TEMP"][:][0, :]
sal = netcdf_data["PSAL"][:][0, :]
pres = netcdf_data["PRES"][:][0, :]


aes_temp = AEE(temp)
aes_sal = AEE(sal)
aes_pres = AEE(pres)


plt.plot(aes_temp, aes_sal, "*")
plt.plot(temp, sal, ".")
plt.savefig("temp_vs_sal.png")
