from ocean_data import (
    read_mat_files_from_path,
    plot_temperature_with_lat_lon,
    filter_temperature,
    make_gif,
)


temperature_path = "tests/data/2015_sst_mountly.mat"
longitude_path = "tests/data/longitud.mat"
latitude_path = "tests/data/latitud.mat"

temperature = read_mat_files_from_path(temperature_path, "CompSST")
longitude = read_mat_files_from_path(longitude_path, "varlon")[:, :]
latitude = read_mat_files_from_path(latitude_path, "varlat")[:, :]

temp_max = 33
temp_min = 21

months = 12
for i in range(months):
    month_number = i
    temperature_month = temperature[:, :, month_number]
    filtered_temperature_month = filter_temperature(temperature_month, temp_max, temp_min)

    filename = f"figures/temperatura_{month_number + 1}.png"
    plot_temperature_with_lat_lon(longitude, latitude, filtered_temperature_month, filename)
