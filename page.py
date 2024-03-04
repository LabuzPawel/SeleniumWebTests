from selenium.webdriver.common.by import By
from element import BasePageElement
from locator import MainPageLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

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
    
    def Cookies(self):
        time.sleep(1)
        cookie_iframe = self.driver.find_element(*MainPageLocator.Cookies_iframe)
        self.driver.switch_to.frame(cookie_iframe)
        time.sleep(1)
        
        element = self.driver.find_element(*MainPageLocator.Cookies_manage_button)
        element.click()
        time.sleep(1)
        self.driver.switch_to.default_content()

        cookie_iframe2 = self.driver.find_element(*MainPageLocator.Cookies_iframe2)
        self.driver.switch_to.frame(cookie_iframe2)
        element = self.driver.find_element(*MainPageLocator.Cookies_manage_site_vendors)
        element.click()
        time.sleep(1)

        element = self.driver.find_element(*MainPageLocator.Cookies_manage_facebook)
        element.click()
        time.sleep(1)

        element = self.driver.find_element(*MainPageLocator.Cookies_manage_facebook_switch)
        element.click()
        time.sleep(1)
        return 'Consent Purposes' in self.driver.page_source
    
    def schedule(self):
        time.sleep(1)
        cookie_iframe = self.driver.find_element(By.ID, "sp_message_iframe_1033523")
        self.driver.switch_to.frame(cookie_iframe)
        time.sleep(1)

        element = self.driver.find_element(*MainPageLocator.Cookies_accept_button)
        element.click()
        time.sleep(1)

        actions = ActionChains(self.driver)
        element = self.driver.find_element(*MainPageLocator.schedule_frontpage)
        actions.move_to_element(to_element=element)
        actions.perform()
        time.sleep(1) 

        element = self.driver.find_element(*MainPageLocator.schedule_frontpage_full)       
        actions.move_to_element(to_element=element)
        actions.click()
        actions.perform()
        time.sleep(1)

        element = self.driver.find_element(*MainPageLocator.schedule_2023)
        element.click()
        time.sleep(1)

        count = 1
        schedule_2023_list = []
        for x in range(23):
            round = 'ROUND ' + str(count)
            selector = 'a[data-roundtext="' + round + '"]'
            element = self.driver.find_element(By.CSS_SELECTOR, selector)
            atr = element.get_attribute('data-racecountryname')
            count += 1
            schedule_2023_list.append(atr)
        return schedule_2023_list == ['Bahrain', 'Saudi Arabia', 'Australia', 'Azerbaijan', 'United States', 'Italy', 'Monaco', 'Spain', 'Canada', 'Austria', 'Great Britain', 'Hungary', 'Belgium', 'Netherlands', 'Italy', 'Singapore', 'Japan', 'Qatar', 'United States', 'Mexico', 'Brazil', 'United States', 'Abu Dhabi']
    
# class SearchResultPage(BasePage):
#     def is_result_found(self):
#         WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'appbar')))
#         return '' not in self.driver.page_source