from pickle import FRAME

from Library.selenium_wrapper import SeleniumWrapper
from Library.selenium_wrapper import outer
from Data.excel_reading import search_data
from POM.locators import LOCATORS
# item = search_data()
# print(item)
class Search():
    def __init__(self,driver):
        self.driver = driver
        self.wrapper_obj = SeleniumWrapper(self.driver)
    @outer
    def search(self,data):
        self.wrapper_obj.click_on_element(LOCATORS["search_home"])
        self.wrapper_obj.enter_data(LOCATORS["enter_data"],data)
        self.wrapper_obj.click_on_element(LOCATORS["search_button"])
        self.wrapper_obj.wait_for_element([LOCATORS["enter_data"]])


    # @outer
    # def enter_data(self,data):
    #     # self.wrapper_obj.click_on_element(('xpath', '//span[text()="PlayStation.com"]'))
    #     self.wrapper_obj.enter_data(('xpath','//input[@type="search"]'),data)
    #     self.wrapper_obj.click_on_element(('xpath','//button[@class="dtm-no-track jetstream-search__search-button"]'))
    #
    # def click_on_sites(self,data1):
    #     self.click_on_search()
    #     self.wrapper_obj.click_on_element(('xpath','//button[@aria-label="Choose a site to search."]'))
    #     self.wrapper_obj.click_on_element(('xpath','//button[@data-qa="select-option-store"]'))
    #     self.wrapper_obj.enter_data(('xpath', '//input[@type="search"]'),data1)
    #     self.wrapper_obj.click_on_element(('xpath', f'//span[text()="{data1}"]'))
    #

