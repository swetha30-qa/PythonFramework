import pytest

from POM import banner
from POM.banner import MainBanner
from test_execution.conftest import drivers

@pytest.mark.smoke
def test_banner(drivers):
    ban_obj = MainBanner(drivers)
    ban_obj.click_on_banner()
    assert "Latest" in drivers.page_source,"Banner is not loaded correctly"
    # assert "Add to Cart" in drivers.page_source ,"Deal page is not loaded correctly"
    # ban_obj.click_on_banner1()
    # ban_obj.click_on_banner2()

