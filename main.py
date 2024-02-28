import unittest
from selenium import webdriver
import page

class GoogleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com/')
        self.driver.implicitly_wait(1)

    def test_google_1(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
    
    def test_google_2(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_TandC_button()
        mainPage.Search_Text_Element = 'test'
        mainPage.click_search_button()
        self.driver.implicitly_wait(10)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()