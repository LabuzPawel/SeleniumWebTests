from selenium.webdriver.common.by import By
from element import BasePageElement
from locator import MainPageLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchTextElement(BasePageElement):
    locator = 'q'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    Search_Text_Element = SearchTextElement()

    def is_title_matches(self):
        title = self.driver.title
        return title == 'F1 - The Official Home of Formula 1® Racing'
    
    def TandC(self):
        time.sleep(2)
        cookie_iframe = self.driver.find_element(By.ID, "sp_message_iframe_1033523")
        self.driver.switch_to.frame(cookie_iframe)
        time.sleep(2)
        
        element = self.driver.find_element(*MainPageLocator.TandC_manage_button)
        element.click()
        time.sleep(3)
        self.driver.switch_to.default_content()

        cookie_iframe2 = self.driver.find_element(By.ID, "sp_message_iframe_814265")
        self.driver.switch_to.frame(cookie_iframe2)
        element = self.driver.find_element(*MainPageLocator.TandC_manage_site_vendors)
        element.click()
        time.sleep(2)

        element = self.driver.find_element(*MainPageLocator.TandC_manage_facebook)
        element.click()
        time.sleep(2)

        element = self.driver.find_element(*MainPageLocator.TandC_manage_facebook_switch)
        element.click()
        time.sleep(2)
        return 'Consent Purposes' in self.driver.page_source
    
class SearchResultPage(BasePage):
    def is_result_found(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'appbar')))
        return 'odnaleziona.' not in self.driver.page_source