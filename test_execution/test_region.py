import pytest

from POM import region
@pytest.mark.sanity
def test_region(drivers):
    reg_obj = region.Region(drivers)
    reg_obj.select_region()
    assert "en-in" in drivers.current_url ,"Page is not loaded"