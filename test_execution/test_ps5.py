import pytest

from POM import ps5
@pytest.mark.smoke
def test_slider_click(drivers):
    ps5_obj = ps5.PS5(drivers)
    ps5_obj.click_on_slide()
    assert " PlayStation 5 Pro " in drivers.page_source ,"Page is not loaded"