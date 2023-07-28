from ocean_data import read_netcdf_from_path, get_latitude_and_longitude, extract_variable, plot_variable_with_lat_lon

import numpy as np

netcdf_file = "GEBCO_27_Jul_2023_592d9805db38/gebco_2023_n32.0_s25.0_w-116.0_e-106.0.nc"

variable_name = "elevation"
netcdf_data = read_netcdf_from_path(netcdf_file)
longitude, latitude = get_latitude_and_longitude(netcdf_data)
variable = np.float32(extract_variable(variable_name, netcdf_data))
filename = f"{variable_name}.png"
plot_variable_with_lat_lon(longitude, latitude, variable, filename)

