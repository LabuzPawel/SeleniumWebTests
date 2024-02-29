import unittest
from selenium import webdriver
import page
from locator import MainPageLocator
import time

class website_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.formula1.com/')
        self.driver.implicitly_wait(1)

    def test_formula1_title(self):                                                          #title test
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
    
    def test_formula1_Cookies(self):                                                        #Cookies test
        mainPage = page.MainPage(self.driver)
        assert mainPage.Cookies()
        
        element = self.driver.find_element(*MainPageLocator.Cookies_manage_save_choices)
        element.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()