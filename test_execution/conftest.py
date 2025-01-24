import time
import os
import random
from pytest import fixture
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.edge.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser",action = "store",dest = "browser_name",default="edge")
    parser.addoption("--timeout",action = "store",dest = "max_time",default = 10)

@fixture()
def drivers(request):
    browser_class = request.config.option.browser_name
    if browser_class.upper() == "EDGE":
        driver = Edge()
    elif browser_class.upper() == "CHROME":
        driver = Chrome()
    else:
        raise Exception("Unkown Browser")

    driver.maximize_window()
    driver.implicitly_wait(50)
    driver.get('https://www.playstation.com/en-sg/')
    egde_option = Options()
    egde_option.add_argument("--disable-notifications")
    yield driver
    time.sleep(3)
    driver.close()



def pytest_runtest_makereport(item,call):
    if call.when == 'call' and call.excinfo is not None:
        driver_ = item.funcargs.get('drivers')
        if driver_:
            screenshot_dir = "Screenshots"
            os.makedirs(screenshot_dir,exist_ok=True)
            random_number = random.randint(1000,9999)
            screenshot_file = f'{screenshot_dir}/{item.name}_{random_number}.png'
            driver_.save_screenshot(screenshot_file)
            print(f'Screenshot saved for failed test:{screenshot_file}')
