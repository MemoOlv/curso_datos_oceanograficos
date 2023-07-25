from ocean_data import (
    build_file_number,
    build_url,
    build_filename,
    download_file,
    build_julian_string,
)
import os


def test_download_file():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    output_file = "tests/data/iris_data.csv"
    remove_download_file(output_file)
    download_file(url, output_file)
    assert os.path.exists(output_file)
    remove_download_file(output_file)


def test_build_url():
    day_number = 1
    year = 2014
    obtained = build_url(day_number, year)
    expected = "https://www.ncei.noaa.gov/data/oceans/ghrsst/L4/GLOB/JPL/MUR25/2014/001/20140101090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc"
    assert obtained == expected

    day_number = "365"
    obtained = build_url(day_number, year)
    expected = "https://www.ncei.noaa.gov/data/oceans/ghrsst/L4/GLOB/JPL/MUR25/2014/365/20141231090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc"
    assert obtained == expected


def test_build_julian_string():
    year = 2014
    julian_day = 365
    obtained = build_julian_string(year, julian_day)
    expected = "20141231"
    assert obtained == expected


def test_build_filename():
    day_number = "001"
    obtained = build_filename(day_number)
    expected = "file_001.nc"
    assert obtained == expected

    day_number = "001"
    directory = "tests/data/"
    obtained = build_filename(day_number, directory)
    expected = "tests/data/file_001.nc"
    assert obtained == expected


def test_build_file_number():
    number = 1
    obtained = build_file_number(number)
    expected = "001"
    assert obtained == expected

    number = 20
    obtained = build_file_number(number)
    expected = "020"
    assert obtained == expected


def remove_download_file(download_file_path):
    if os.path.exists(download_file_path):
        os.remove(download_file_path)
