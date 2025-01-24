from Library.selenium_wrapper import SeleniumWrapper
from POM.locators import LOCATORS_SIGNIN
class Signin:
    def __init__(self,driver):
        self.driver = driver
        self.wraper_obj = SeleniumWrapper(self.driver)

    def click_on_signin(self,data):
        self.wraper_obj.click_on_element(LOCATORS_SIGNIN["click_signin"])
        self.wraper_obj.click_on_element(LOCATORS_SIGNIN["click_account"])
        self.wraper_obj.click_on_element(LOCATORS_SIGNIN["click_create"])
        self.wraper_obj.click_on_element(LOCATORS_SIGNIN["select_country"])
        self.wraper_obj.select_item(LOCATORS_SIGNIN["click_country"],"India")
        self.wraper_obj.wait_for_element(LOCATORS_SIGNIN["wait_ele"])
        # self.wraper_obj.click_on_element(LOCATORS_SIGNIN["click_lang"])

        self.wraper_obj.click_on_element(LOCATORS_SIGNIN["click_next"])
        # self.wraper_obj.click_on_element(LOCATORS_SIGNIN["click_day"])

    # def click_on_signin_date(self,data):
    #     self.wraper_obj.wait_for_element(LOCATORS_SIGNIN["select_date"])
    #     self.wraper_obj.select_item(LOCATORS_SIGNIN["select_date"], "2")




