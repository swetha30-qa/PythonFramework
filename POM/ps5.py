from Library import selenium_wrapper
from Library.selenium_wrapper import SeleniumWrapper
from selenium.webdriver.common.action_chains import ActionChains
from POM.locators import LOCATORS_PS5


class PS5():
    def __init__(self,driver):
        self.driver = driver
        self.wrapper_obj = SeleniumWrapper(self.driver)
        self.actn_obj = ActionChains(self.driver)


    def click_on_slide(self):
        self.wrapper_obj.wait_for_element(LOCATORS_PS5["wait_ele"])
        self.wrapper_obj.move_element(LOCATORS_PS5["move_ele"])
        # self.wrapper_obj.click_on_element(('xpath','(//div[text()=" Find out more "])[1]'))
        # if id == 3:
        self.wrapper_obj.click_on_element(LOCATORS_PS5["ps5"])
        self.wrapper_obj.click_on_element(LOCATORS_PS5["click_ele"])

        # id = 1
        # while True:
        #      if id == 3:
        #         self.wrapper_obj.click_on_element(('xpath',f'//div[@data-control-id="{id}"]'))
        #         # self.wrapper_obj.click_on_element(('xpath','//a[contains(@data-uuid,"3a5c597")]'))
        #         id += 1


