from ocean_data import plot_netcdf_files

import numpy as np

netcdf_file = ["GEBCO_27_Jul_2023_592d9805db38/gebco_2023_n32.0_s25.0_w-116.0_e-106.0.nc"]

variable_name = "elevation"
plot_netcdf_files(netcdf_file, variable_name)
