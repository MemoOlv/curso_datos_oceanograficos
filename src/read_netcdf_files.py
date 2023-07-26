from ocean_data import read_netcdf_from_path, plot_temperature_with_lat_lon

netcdf_path = "tests/data/SST_20200111.nc"

netcdf_data = read_netcdf_from_path(netcdf_path)
temperature = netcdf_data["analysed_sst"][0][:, :]
longitude = netcdf_data["longitude"][:]
latitude = netcdf_data["latitude"][:]

filename = "temperature_from_netcdf"
plot_temperature_with_lat_lon(longitude, latitude, temperature, filename)
