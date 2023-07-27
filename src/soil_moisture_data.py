from ocean_data import read_netcdf_from_path, plot_variable_with_lat_lon, get_latitude_and_longitude


netcdf_file = "tests/data/ESACCI-SOILMOISTURE-L3S-SSMV-COMBINED-20220101000000-fv08.1.nc"
netcdf_data = read_netcdf_from_path(netcdf_file)

longitude, latitude = get_latitude_and_longitude(netcdf_data)
longitude_corrected = longitude[:] - 360

soil_moisture = netcdf_data["sm"][0]

filename = "soil_moisture.png"
plot_variable_with_lat_lon(longitude, latitude, soil_moisture, filename)
