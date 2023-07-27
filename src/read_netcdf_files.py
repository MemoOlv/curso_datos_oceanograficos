from ocean_data import read_netcdf_from_path, plot_temperature_with_lat_lon
from glob import glob

netcdf_files = glob("tests/data/SST*.nc")

i = 1
for netcdf_file in netcdf_files:
    netcdf_data = read_netcdf_from_path(netcdf_file)
    temperature = netcdf_data["analysed_sst"][0]
    longitude = netcdf_data["longitude"]
    latitude = netcdf_data["latitude"]

    filename = f"temperature_from_{i}.png"
    plot_temperature_with_lat_lon(longitude, latitude, temperature, filename)
    i += 1

    del temperature
    del longitude
    del latitude
