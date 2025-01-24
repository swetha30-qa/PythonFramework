import pytest

from Data.excel_reading import search_data
from Data.excel_reading import get_games
from POM import search
item = search_data()
item1 = get_games()
@pytest.mark.smoke
@pytest.mark.parametrize("input",item)
def test_search(drivers,input):
    search_obj = search.Search(drivers)
    search_obj.search(input)
    assert input in drivers.page_source, "No result page is loaded"
    if input == "abcxyrd":
        assert "0 results" in drivers.page_source, "Result page is loaded"
