from ocean_data import read_netcdf_from_path


def test_netcdf():
    netcdf_path = "tests/data/SST_20200111.nc"
    netcdf_data = read_netcdf_from_path(netcdf_path)
    obtained_variables = list(netcdf_data.variables.keys())
    expected_variables = ["time", "latitude", "longitude", "analysed_sst", "mask"]
    assert obtained_variables == expected_variables
    