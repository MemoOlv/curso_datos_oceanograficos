import netCDF4
import scipy.io


def read_netcdf_from_path(netcdf_path):
    return netCDF4.Dataset(netcdf_path)


def read_mat_files_from_path(mat_path, variable):
    mat_data = scipy.io.loadmat(mat_path)
    return mat_data[variable]


def get_latitude_and_longitude(netcdf_data):
    variables_keys = netcdf_data.variables.keys()
    lat_key = find_latitude_key(variables_keys)
    lon_key = find_longitude_key(variables_keys)
    longitude = netcdf_data[lon_key]
    latitude = netcdf_data[lat_key]
    return longitude, latitude


def find_longitude_key(variables_keys):
    return [x for x in variables_keys if x.startswith("lon") or x.startswith("Lon")][0]


def find_latitude_key(variables_keys):
    return [x for x in variables_keys if x.startswith("lat") or x.startswith("Lat")][0]


def extract_temporal_dimension(netcdf_data, variable):
    return netcdf_data[variable].shape[0] - 1
