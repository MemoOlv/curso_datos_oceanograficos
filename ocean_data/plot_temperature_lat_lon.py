import matplotlib.pyplot as plt
import numpy as np
import glob
from PIL import Image


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
