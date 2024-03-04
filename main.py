import unittest
from selenium import webdriver
import page
# from locator import MainPageLocator
# import time

class website_test(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://www.formula1.com/')
        
        
    def tearDown(self):
        self.driver.close()

    def test_formula1_title(self):                                                          #title test
        mainPage = page.MainPage(self.driver)
        self.assertTrue(mainPage.is_title_matches())
    
    def test_formula1_Cookies(self):                                                        #Cookies test
        mainPage = page.MainPage(self.driver)
        self.assertTrue(mainPage.Cookies())
        
        # element = self.driver.find_element(*MainPageLocator.Cookies_manage_save_choices)
        # element.click()
        # time.sleep(2)
    
    def test_formula1_schedule(self):                                                       #schedule check
        mainPage = page.MainPage(self.driver)
        self.assertTrue(mainPage.schedule())

if __name__ == '__main__':
    unittest.main()