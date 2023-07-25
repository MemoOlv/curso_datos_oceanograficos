import netCDF4


def read_netcdf_from_path(netcdf_path):
    return netCDF4.Dataset(netcdf_path)
