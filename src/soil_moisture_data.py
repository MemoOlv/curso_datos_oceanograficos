from ocean_data import read_netcdf_from_path, plot_temperature_with_lat_lon


netcdf_file = "tests/data/ESACCI-SOILMOISTURE-L3S-SSMV-COMBINED-20220101000000-fv08.1.nc"
netcdf_data = read_netcdf_from_path(netcdf_file)

soil_moisture = netcdf_data["sm"][0]
longitude = netcdf_data["lon"][:] - 360
latitude = netcdf_data["lat"]

filename = "soil_moisture.png"
plot_temperature_with_lat_lon(longitude, latitude, soil_moisture, filename)
