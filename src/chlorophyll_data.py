from ocean_data import plot_variable_with_lat_lon
import numpy as np


chlorophyll_path = "tests/data/chlorophyll"
longitude_path = "tests/data/Longi"
latitude_path = "tests/data/Lati"

chlorophyll = np.load(chlorophyll_path, allow_pickle=True)
longitude = np.load(longitude_path, allow_pickle=True)
latitude = np.load(longitude_path, allow_pickle=True)


filename = "chlorophyll.png"
plot_variable_with_lat_lon(longitude, latitude, chlorophyll, filename)
