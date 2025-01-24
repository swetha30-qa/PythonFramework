from Library import selenium_wrapper
import time
from Library.selenium_wrapper import SeleniumWrapper
from Library.selenium_wrapper import outer
from POM.exception import ElementNotFoundException
from selenium.webdriver.common.action_chains import ActionChains
from POM.locators import LOCATORS_BANNER
class MainBanner:
    def __init__(self,driver):
        self.driver = driver
        self.wrapper_obj = SeleniumWrapper(driver)
        self.act_obj = ActionChains(self.driver)

    @outer
    def click_on_banner(self):
        # slide_id = 0
        for slide_id in range(0,5):
        # while True:
            try:
                banner_xpath = (LOCATORS_BANNER["click_banner"][0],LOCATORS_BANNER["click_banner"][1].format(slide_id=slide_id,next_slide_id=slide_id+1))
                next_banner_xpath = (LOCATORS_BANNER["click_slide"][0],LOCATORS_BANNER["click_slide"][1].format(next_slide_id=slide_id+1))
                self.wrapper_obj.click_on_element(banner_xpath)
                # if slide_id == 3:
                #     self.driver.back()
                self.navigate_to_home()
                self.wrapper_obj.move_element(next_banner_xpath)
                self.wrapper_obj.click_on_element(next_banner_xpath)
                # slide_id += 1
                # if slide_id == 5:
                #     break

            except:
                raise ElementNotFoundException(f'No banner is found based on the id {slide_id} ')


    def navigate_to_home(self):
            self.wrapper_obj.click_on_element(('xpath', '//a[@aria-label="PlayStation.com"]'))







    # @outer
    # def click_on_banner(self):
    #     for banner, links in item:
    #         if banner == "FY24 Q3 | Global Promo | Holiday January Sale V2 keyart":
    #             self.wrapper_obj.click_on_element(('xpath', f'//img[@alt="{banner}"]'))
    #             self.wrapper_obj.click_on_element(('xpath', f'//span[text()="{links}"]'))
    #             # try:
    #             #
    #             #     element = self.wrapper_obj.click_on_element(('xpath','//span[text()="Browse the deals"]'))
    #             #     return element
    #             # except:
    #             #     raise ElementNotFoundException(f'The element {element} is not found')
    #
    #     # self.wrapper_obj.wait_for_element(('xpath','//h1[text()="Holiday Sale"]'))
    #     self.wrapper_obj.click_on_element(('xpath','(//div[@class="psw-product-tile psw-interactive-root"])[1]'))
    #     self.wrapper_obj.wait_for_element(('xpath','//span[text()="Add to Cart"]'))
    #
    # def click_on_banner1(self):
    #     for banner,links in item:
    #             self.wrapper_obj.click_on_element(('xpath', f'//img[@alt="{banner}"]'))
    #             self.wrapper_obj.click_on_element(('xpath',f'//span[text()="{links}"]'))
    #             self.navigate_to_home()
    #
    # def navigate_to_home(self):
    #         self.wrapper_obj.click_on_element(('xpath', '//a[@aria-label="PlayStation.com"]'))
            # self.driver.wait_for_element(('xpath', '//button[text()="Games"]'))

    # @outer
    # def click_on_banner2(self):
    #     slide_id = 0
    #     while True:
    #         try:
    #
    #             self.wrapper_obj.click_on_element(('xpath',f'//div[@data-slide="{slide_id}"]/../../../..//div[@data-slide-id="{slide_id+1}"]'))
    #             if slide_id == 3:
    #                 self.driver.back()
    #             self.navigate_to_home()
    #             self.wrapper_obj.move_element(('xpath', f'//div[@data-slide="{slide_id + 1}"]'))
    #             self.wrapper_obj.click_on_element(('xpath', f'//div[@data-slide="{slide_id + 1}"]'))
    #             slide_id += 1
    #             if slide_id == 6:
    #                 break
    #         except:
    #             raise ElementNotFoundException(f'No banner is found based on the id {slide_id} ')


    # def click_on_banner(self):
    #     slide_id = 0
    #     while True:
    #         try:
    #             banner_xpath = (LOCATORS_BANNER["click_banner"][0],LOCATORS_BANNER["click_banner"][1].format(slide_id=slide_id,next_slide_id=slide_id+1))
    #             next_banner_xpath = (LOCATORS_BANNER["click_slide"][0],LOCATORS_BANNER["click_slide"][1].format(next_slide_id=slide_id+1))
    #             self.wrapper_obj.click_on_element(banner_xpath)
    #             if slide_id == 3:
    #                 self.driver.back()
    #             self.navigate_to_home()
    #             self.wrapper_obj.move_element(next_banner_xpath)
    #             self.wrapper_obj.click_on_element(next_banner_xpath)
    #             slide_id += 1
    #             if slide_id == 6:
    #                 break
    #         except:
    #             raise ElementNotFoundException(f'No banner is found based on the id {slide_id} ')