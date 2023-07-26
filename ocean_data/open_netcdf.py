import netCDF4
import scipy.io


def read_netcdf_from_path(netcdf_path):
    return netCDF4.Dataset(netcdf_path)


def read_mat_files_from_path(mat_path, variable):
    mat_data = scipy.io.loadmat(mat_path)
    return mat_data[variable]
