import matplotlib.pyplot as plt
import numpy as np
import glob
from PIL import Image

from ocean_data import read_netcdf_from_path, get_latitude_and_longitude, extract_temporal_shape


def plot_netcdf_files(netcdf_files, variable_name):
    for i in range(0, len(netcdf_files)):
        netcdf_data = read_netcdf_from_path(netcdf_files[i])
        longitude, latitude = get_latitude_and_longitude(netcdf_data)
        variable = extract_variable(variable_name, netcdf_data)

        filename = f"{variable_name}_{i+1}.png"
        plot_variable_with_lat_lon(longitude, latitude, variable, filename)

        del variable
        del longitude
        del latitude

def extract_variable(variable_name, netcdf_data):
    temporal_shape = extract_temporal_shape(netcdf_data, variable_name)
    if len(temporal_shape) < 3:
        variable = netcdf_data[variable_name][:,:]
    else:
        variable = netcdf_data[variable_name][temporal_shape]
    return np.float32(variable[:,:])


def plot_variable_with_lat_lon(longitude, latitude, temperature_1, filename):
    fig, ax = plt.subplots()
    ax.pcolor(longitude, latitude, temperature_1)
    ax.set_xlabel("Longitude (ºW)")
    ax.set_ylabel("Latitude (ºN)")
    plt.savefig(filename)


def filter_temperature(temperature_1, temp_max, temp_min):
    filtered_temperature_1 = temperature_1
    filtered_temperature_1[temperature_1 > temp_max] = np.nan
    filtered_temperature_1[temperature_1 < temp_min] = np.nan
    return filtered_temperature_1


def make_gif(frame_folder, gifname):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.png")]
    frame_one = frames[0]
    frame_one.save(gifname, format="GIF", append_images=frames, save_all=True, duration=100, loop=0)
