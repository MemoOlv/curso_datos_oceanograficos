from ocean_data import (
    read_netcdf_from_path,
    read_mat_files_from_path,
    find_longitude_key,
    find_latitude_key,
    extract_temporal_shape,
    extract_variable
)


import numpy as np

netcdf_path = "tests/data/SST_20200111.nc"
netcdf_data = read_netcdf_from_path(netcdf_path)


def test_read_netcdf_from_path():
    obtained_variables = list(netcdf_data.variables.keys())
    expected_variables = ["time", "latitude", "longitude", "analysed_sst", "mask"]
    assert obtained_variables == expected_variables


def test_read_mat_files_from_path():
    mat_path = "tests/data/longitud.mat"
    variable = "varlon"
    obtained_longitude = read_mat_files_from_path(mat_path, variable)
    assert obtained_longitude.shape == (1113, 779)

    mat_path = "tests/data/latitud.mat"
    variable = "varlat"
    obtained_longitude = read_mat_files_from_path(mat_path, variable)
    assert obtained_longitude.shape == (1113, 779)


def test_find_longitude_key():
    variable_key = "lon"
    variables_keys = {variable_key: []}
    obtained = find_longitude_key(variables_keys)
    assert obtained == variable_key

    variable_key = "Longitude"
    variables_keys = {variable_key: []}
    obtained = find_longitude_key(variables_keys)
    assert obtained == variable_key


def test_find_latitude_key():
    variable_key = "lat"
    variables_keys = {variable_key: []}
    obtained = find_latitude_key(variables_keys)
    assert obtained == variable_key

    variable_key = "Latitude"
    variables_keys = {variable_key: []}
    obtained = find_latitude_key(variables_keys)
    assert obtained == variable_key


def test_extract_temporal_shape():
    expected_dimension = (1,501, 1401)
    variable = "analysed_sst"
    obtained_dimension = extract_temporal_shape(netcdf_data, variable)
    assert obtained_dimension == expected_dimension


def test_extract_variable():
    netcdf_path = "tests/data/gebco_2023_n32.0_s25.0_w-116.0_e-106.0.nc"
    netcdf_data = read_netcdf_from_path(netcdf_path)
    variable_name = "elevation"
    obtained = extract_variable(variable_name, netcdf_data)
    expected_shape = (1680, 2400)
    obtained_shape = obtained.shape
    assert obtained_shape == expected_shape
