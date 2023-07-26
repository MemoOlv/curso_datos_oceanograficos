import netCDF4


def read_netcdf_from_path(netcdf_path):
    return netCDF4.Dataset(netcdf_path)

def read_mat_files_from_path(mat_path):
    pass