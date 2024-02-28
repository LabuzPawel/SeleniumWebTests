from selenium.webdriver.common.by import By
from element import BasePageElement
from locator import MainPageLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchTextElement(BasePageElement):
    locator = 'q'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    Search_Text_Element = SearchTextElement()

    def is_title_matches(self):
        title = self.driver.title
        return title == 'Google'
    
    def click_TandC_button(self):
        element = self.driver.find_element(*MainPageLocator.TandC_button)
        element.click()
    
    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocator.search_button)
        element.click()
    
class SearchResultPage(BasePage):
    def is_result_found(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'appbar')))
        return 'odnaleziona.' not in self.driver.page_source