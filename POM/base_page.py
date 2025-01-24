from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait_obj = WebDriverWait(self.driver,30)

    def click_on_element(self,logical_name):
        self.driver.find_element(*logical_name).click()

    def wait_for_element(self,logical_name):
        try:
            element = self.wait_obj.until(expected_conditions.presence_of_element_located(logical_name))
            return element
        except Exception as e:
            print(f"Error is :{e}")

    # def get_links(self,logical_name):
    #     links = self.driver.find_elements(logical_name)
    #     links_iter = iter(links)
    #     for i in links_iter:
    #         print(links_iter.text)




