import pytest
from POM.category import Category
@pytest.mark.smoke
def test_category(drivers):
    cate_obj = Category(drivers)
    cate_obj.click_on_category1()
    assert "https://www.playstation.com/en-sg/" in drivers.current_url,"The main page URL is incorrect"

@pytest.mark.smoke
def test_subcategory(drivers):
    sub_obj = Category(drivers)
    sub_obj.click_on_cat_sub()
    assert "PlayStation®5" in drivers.page_source ,"PS5 Subcategory is not loaded correctly"
#
#
@pytest.mark.sanity
def test_home_page(drivers):
    drivers.get('https://www.playstation.com/en-sg/')
    assert "playstation.com" in drivers.current_url,"Main page URL is incorrect"
    # assert drivers.find_element(('xpath','//a[@aria-label="PlayStation.com"]')).is_displayed(),"PlayStaion logo is not visible"
#
# @pytest.mark.sanity
# def test_click_category(drivers):
#     cate_obj = Category(drivers)
#     cate_obj.click_on_category()
#     assert "Games" in drivers.page_source,"Games Category not displayed correclty"
#
@pytest.mark.sanity
def test_clck_subcategory(drivers):
    cate_obj = Category(drivers)
    sub_obj = Category(drivers)
    cate_obj.click_on_category()
    assert "Games" in drivers.page_source, "Games Category not displayed correclty"
    sub_obj.click_on_cat_sub()
    assert "PlayStation®5" in drivers.page_source,"PS5 subcategories page did not load correctly"

# @pytest.mark.sanity
# def test_click_cat_sub(drivers):
#     sub_obj = Category(drivers)
#     sub_obj.click_on_category_and_subcategories()
#     assert "PlayStation®5" in drivers.page_source, "PS5 subcategories page did not load correctly"
#     sub_obj.navigate_to_home()
#     sub_obj.click_on_category_and_subcategories()
#     assert "ps4" in drivers.current_url,"PS4 subcategories page did not load correctly"


# def test_links(drivers):
#     cate_obj = Category(drivers)
#     cate_obj.count_links()