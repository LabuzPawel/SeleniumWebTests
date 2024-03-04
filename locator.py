from selenium.webdriver.common.by import By

class MainPageLocator(object):
    Cookies_manage_button = (By.XPATH, '//*[@id="notice"]/div[3]/button[1]')
    Cookies_reject_button = (By.XPATH, "//button[@title='REJECT ALL']")
    Cookies_accept_button = (By.XPATH, "//button[@title='ACCEPT ALL']")
    Cookies_manage_site_vendors = (By.XPATH, "html/body/div/div[2]/div[5]/div[1]/div[3]")
    Cookies_manage_facebook = (By.XPATH, '/html/body/div/div[2]/div[5]/div[2]/div/div[4]/div[1]/button[1]')
    Cookies_manage_facebook_consent = (By.XPATH, '//*[@id="28602"]/p/div/div[2]/div/div[1]/h3')
    Cookies_manage_facebook_switch = (By.CSS_SELECTOR, 'body > div > div.message.type-modal > div.message-component.message-stacks.privacy-manager-tcfv2.no-children.p > div.pm-section > div > div:nth-child(4) > div.stack-row.custom > button.pm-switch')
    Cookies_manage_save_choices = (By.XPATH, "//button[@title='SAVE YOUR CHOICES']")

    schedule_frontpage = (By.XPATH, "//*[@id='primaryNav']/div/div[2]/ul/li[4]")
    schedule_frontpage_full = (By.XPATH, '//*[@id="primaryNav"]/div/div[2]/ul/li[4]/div/div/div/div/div[1]/a[1]')
    schedule_2023 = (By.XPATH, '/html/body/div[2]/main/div/div/div[3]/div/div/div/a')

class SearchResultPageLocators(object):
    pass