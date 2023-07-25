import requests
import os
from datetime import datetime


def download_from_day(day_number, year, directory):
    file_number_for_day = build_file_number(day_number)
    url = build_url(file_number_for_day, year)
    create_directory(directory)
    output_file = build_filename(file_number_for_day, directory)
    print("Descarga: ", url)
    download_file(url, output_file)


def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def download_file(url: str, output_file: str):
    response = requests.request("GET", url)
    open(output_file, "wb").write(response.content)


def build_file_number(day_number: int) -> str:
    return str(day_number).rjust(3, "0")


def build_julian_string(year: int, julian_day: int) -> str:
    julian_day = f"{year}{julian_day}"
    format = "%Y%j"
    date_year_month_day = datetime.strptime(julian_day, format).date()
    return str(date_year_month_day).replace("-", "")


def build_url(day_number: int, year: int) -> str:
    day_number_folder = build_file_number(day_number)
    julian_date = build_julian_string(year, day_number)
    return f"https://www.ncei.noaa.gov/data/oceans/ghrsst/L4/GLOB/JPL/MUR25/{year}/{day_number_folder}/{julian_date}090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc"


def build_filename(day_number: str, directory: str = "") -> str:
    return directory + f"file_{day_number}.nc"


def remove_download_file(download_file_path):
    if os.path.exists(download_file_path):
        os.remove(download_file_path)
