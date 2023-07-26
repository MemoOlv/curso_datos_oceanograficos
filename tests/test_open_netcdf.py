from ocean_data import read_netcdf_from_path, read_mat_files_from_path


def test_read_netcdf_from_path():
    netcdf_path = "tests/data/SST_20200111.nc"
    netcdf_data = read_netcdf_from_path(netcdf_path)
    obtained_variables = list(netcdf_data.variables.keys())
    expected_variables = ["time", "latitude", "longitude", "analysed_sst", "mask"]
    assert obtained_variables == expected_variables


def test_read_mat_files_from_path():
    mat_path = "tests/data/2015_sst_mountly.mat"
    mat_data = read_mat_files_from_path(mat_path)
    mat_data.keys()
