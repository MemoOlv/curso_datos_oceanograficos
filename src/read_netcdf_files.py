from ocean_data import read_netcdf_from_path, plot_temperature_with_lat_lon, get_latitude_and_longitude
from glob import glob

netcdf_files = glob("tests/data/SST*.nc")


def plot_netcdf_files(netcdf_files, variable):
    for i in range(0, len(netcdf_files)):
        netcdf_data = read_netcdf_from_path(netcdf_files[i])
        longitude, latitude = get_latitude_and_longitude(netcdf_data)
        temperature = netcdf_data[variable][0]

        filename = f"temperature_from_{i+1}.png"
        plot_temperature_with_lat_lon(longitude, latitude, temperature, filename)

        del temperature
        del longitude
        del latitude

plot_netcdf_files(netcdf_files, "analysed_sst")
