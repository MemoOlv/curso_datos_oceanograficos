from ocean_data import read_netcdf_from_path


def test_netcdf():
    netcdf_path = "tests/data/SST_20200111.nc"
    read_netcdf_from_path(netcdf_path)
