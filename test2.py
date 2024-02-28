from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://www.google.com")
actions = ActionChains(driver)
title = driver.title
driver.implicitly_wait(0.5)
# print(title)
TandC = driver.find_element(By.ID, 'L2AGLb')
TandC.click()
assert title == "Google"
# actions.click(on_element=TandC).perform()
driver.implicitly_wait(0.5)
search = driver.find_element(By.ID, 'APjFqb')
search.send_keys('asdg fhj kjsa ddfgh32423 43424243')
search.send_keys(Keys.RETURN)
def aaa():
    test = 'odnaleziona.' not in driver.page_source
    print(test)
    return test
aaa()


driver.quit()

