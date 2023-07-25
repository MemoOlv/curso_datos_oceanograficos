from ocean_data import download_from_day


year = 2014
directory = f"descargas/{year}/"
for day_number in range(12):
    download_from_day(day_number + 1, year, directory)
