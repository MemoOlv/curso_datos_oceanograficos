from ocean_data import read_mat_files_from_path, plot_temperature_with_lat_lon, filter_temperature


temperature_path = "tests/data/2015_sst_mountly.mat"
longitude_path = "tests/data/longitud.mat"
latitude_path = "tests/data/latitud.mat"

temperature = read_mat_files_from_path(temperature_path, "CompSST")
longitude = read_mat_files_from_path(longitude_path, "varlon")[:, :]
latitude = read_mat_files_from_path(latitude_path, "varlat")[:, :]

temperature_1 = temperature[:, :, 0]

temp_max = 33
temp_min = 21
filtered_temperature_1 = filter_temperature(temperature_1, temp_max, temp_min)

file_name = "temperatura_1.png"
plot_temperature_with_lat_lon(longitude, latitude, filtered_temperature_1, "temperatura_1.png")
