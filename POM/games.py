from Library.selenium_wrapper import SeleniumWrapper
from POM.locators import LOCATORS_GAMES
class Games:
    def __init__(self,driver):
        self.driver = driver
        self.wrapper_obj = SeleniumWrapper(self.driver)

    def click_on_deals(self):
        self.wrapper_obj.move_element(LOCATORS_GAMES["move_element"])
        self.wrapper_obj.click_on_element(LOCATORS_GAMES["select_element"])
        self.wrapper_obj.click_on_element(LOCATORS_GAMES["click_banner"])
        self.wrapper_obj.wait_for_element(LOCATORS_GAMES["wait_deal"])
        self.wrapper_obj.click_on_element(LOCATORS_GAMES["click_deal"])
        self.wrapper_obj.wait_for_element(LOCATORS_GAMES["wait_addtocart"])
