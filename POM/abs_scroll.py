from abc import ABC,abstractmethod
from Library.selenium_wrapper import SeleniumWrapper
class Home(ABC):
    def __init__(self,driver):
        self.driver = driver

    @abstractmethod
    def click_on_signin(self):
        pass

