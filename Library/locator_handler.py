class LocatorHandler:
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,logical_name):
        return self.driver.find_element(*logical_name)