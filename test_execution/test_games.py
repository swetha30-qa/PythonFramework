import pytest

from POM.games import Games

@pytest.mark.sanity
def test_game(drivers):
    game_obj = Games(drivers)
    game_obj.click_on_deals()
    assert "items" in drivers.page_source,"Deal page is not loaded correctly"
    assert "Add to Cart" in drivers.page_source, "Game page is not loaded correctly"