from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from Library.locator_handler import LocatorHandler

def outer(func):
    def wrapper(*args,**kwargs):
        print(f"Executing:{func.__name__}")
        result = func(*args,**kwargs)
        print(f"Executed:{func.__name__}")
        return result
    return wrapper


class SeleniumWrapper:
    def __init__(self,driver):
        self.wait_obj = WebDriverWait(driver,30)
        self.driver = driver
        self.actn_obj = ActionChains(driver)
        self.locobj = LocatorHandler(driver)

    @outer
    def click_on_element(self,logical_name):
        ele = self.locobj.get_element(logical_name)
        ele.click()

    @outer
    def enter_data(self,logical_name,data):
        ele = self.locobj.get_element(logical_name)
        ele.send_keys(data)
        self.wait_for_element(logical_name)

    @outer
    def wait_for_element(self,logical_name):
        try:
            element = self.wait_obj.until(expected_conditions.presence_of_element_located(logical_name))
            return element
        except Exception as e:
            print(f"Error is :{e}")

    def select_item(self,logical_name,data):
        element = self.locobj.get_element(logical_name)
        select = Select(element)
        select.select_by_visible_text(data)

    def move_element(self,logical_name):
        element = self.locobj.get_element(logical_name)
        self.actn_obj.move_to_element(element).perform()