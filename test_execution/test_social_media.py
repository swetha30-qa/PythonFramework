import pytest

from POM import social_media
@pytest.mark.sanity
def test_youtube(drivers):
    yotb_obj = social_media.SocialMedia(drivers)
    yotb_obj.click_on_youtube()
    assert "youtube.com" in drivers.current_url ,"Page is not loaded"