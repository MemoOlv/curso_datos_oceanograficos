from ocean_data import read_netcdf_from_path, plot_variable_with_lat_lon, get_latitude_and_longitude, extract_temporal_dimension
from glob import glob

netcdf_files = glob("tests/data/SST*.nc")


def plot_netcdf_files(netcdf_files, variable_name):
    for i in range(0, len(netcdf_files)):
        netcdf_data = read_netcdf_from_path(netcdf_files[i])
        longitude, latitude = get_latitude_and_longitude(netcdf_data)
        temporal_dimension = extract_temporal_dimension(netcdf_data, variable_name)
        variable = netcdf_data[variable_name][temporal_dimension]

        filename = f"{variable_name}_{i+1}.png"
        plot_variable_with_lat_lon(longitude, latitude, variable, filename)

        del variable
        del longitude
        del latitude

plot_netcdf_files(netcdf_files, "analysed_sst")
