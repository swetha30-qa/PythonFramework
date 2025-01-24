from Library.selenium_wrapper import SeleniumWrapper
from POM.locators import LOCATORS_SOCIAL
class SocialMedia:
    def __init__(self,driver):
        self.driver = driver
        self.wraper_obj = SeleniumWrapper(self.driver)

    def click_on_youtube(self):
        self.wraper_obj.move_element(LOCATORS_SOCIAL["move_element"])
        self.wraper_obj.click_on_element(LOCATORS_SOCIAL["click_youtube"])
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])
