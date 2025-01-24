from POM.base_page import BasePage
from POM.locators import LOCATORS_CAT
from Data.excel_reading import get_data
item = get_data()
class Category(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.obj = BasePage(self.driver)


    def click_on_category(self):
        for cat,sub in item:
            element = (LOCATORS_CAT["click_category"][0],LOCATORS_CAT["click_category"][1].format(category=cat))
            print(f'Clicking category{cat}')
            self.obj.click_on_element(element)
            self.obj.wait_for_element(element)
            element1 = (LOCATORS_CAT["click_subcategory"][0],LOCATORS_CAT["click_subcategory"][1].format(subcategory=sub))
            print(sub)
            self.obj.click_on_element(element1)
            self.obj.wait_for_element(element1)
            self.navigate_to_home()


    # def click_on_category_and_subcategories(self):
    #
    #     for category,subcategory in item:
    #         element = self.obj.click_on_element(('xpath', f'//button[text()="{category}"]'))
    #         self.obj.wait_for_element(element)
    #         element1 = self.obj.click_on_element(('xpath', f'//span[text()="{subcategory}"]'))
    #         self.obj.wait_for_element(element1)
    #         self.navigate_to_home()
    #
    #
    def navigate_to_home(self):
        self.obj.click_on_element(LOCATORS_CAT["click_playstation"])
        # self.obj.wait_for_element(LOCATORS_CAT["wait_games"])

    def click_on_category1(self):
        for category, subcategory in item:
            element = self.obj.click_on_element(('xpath', f'//button[text()="{category}"]'))
            self.obj.wait_for_element(element)

    def click_on_cat_sub(self):
        for category, subcategory in item:
            element = self.obj.click_on_element(('xpath', f'//button[text()="{category}"]'))
            self.obj.wait_for_element(element)
            element1 = self.obj.click_on_element(('xpath', f'//span[text()="{subcategory}"]'))
            self.obj.wait_for_element(element1)
            self.navigate_to_home()



