import matplotlib.pyplot as plt
import numpy as np


def plot_temperature_with_lat_lon(longitude, latitude, temperature_1, filename):
    plt.pcolor(longitude, latitude, temperature_1)
    plt.xlabel("Longitude (ºW)")
    plt.ylabel("Latitude (ºN)")
    plt.grid()
    plt.colorbar()
    plt.clim(25, 30)
    plt.savefig(filename)


def filter_temperature(temperature_1, temp_max, temp_min):
    filtered_temperature_1 = temperature_1
    filtered_temperature_1[temperature_1 > temp_max] = np.nan
    filtered_temperature_1[temperature_1 < temp_min] = np.nan
    return filtered_temperature_1
