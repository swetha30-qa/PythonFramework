from Library.selenium_wrapper import SeleniumWrapper
from POM.locators import LOCATORS_REGION
class Region:
    def __init__(self,driver):
        self.driver = driver
        self.wraper_obj = SeleniumWrapper(self.driver)

    def select_region(self):
        self.driver.execute_script("window,scrollTo(0,document.body.scrollHeight)")
        self.wraper_obj.click_on_element(LOCATORS_REGION["change_region"])
        self.wraper_obj.move_element(LOCATORS_REGION["wait_ele"])
        self.wraper_obj.click_on_element(LOCATORS_REGION["select_region"])
        self.wraper_obj.wait_for_element(LOCATORS_REGION["wait_element"])