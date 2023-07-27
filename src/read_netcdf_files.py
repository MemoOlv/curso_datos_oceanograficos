from ocean_data import plot_netcdf_files
from glob import glob

netcdf_files = glob("tests/data/SST*.nc")

plot_netcdf_files(netcdf_files, "analysed_sst")
