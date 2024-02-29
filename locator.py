from selenium.webdriver.common.by import By

class MainPageLocator(object):
    TandC_manage_button = (By.XPATH, "//button[@title='NO, MANAGE SETTINGS']")
    TandC_reject_button = (By.XPATH, "//button[@title='REJECT ALL']")
    TandC_accept_button = (By.XPATH, "//button[@title='ACCEPT ALL']")
    TandC_manage_site_vendors = (By.XPATH, "html/body/div/div[2]/div[5]/div[1]/div[3]")
    TandC_manage_facebook = (By.XPATH, '/html/body/div/div[2]/div[5]/div[2]/div/div[4]/div[1]/button[1]')
    TandC_manage_facebook_consent = (By.XPATH, '//*[@id="28602"]/p/div/div[2]/div/div[1]/h3')
    TandC_manage_facebook_switch = (By.CSS_SELECTOR, 'body > div > div.message.type-modal > div.message-component.message-stacks.privacy-manager-tcfv2.no-children.p > div.pm-section > div > div:nth-child(4) > div.stack-row.custom > button.pm-switch')
    TandC_manage_save_choices = (By.XPATH, "//button[@title='SAVE YOUR CHOICES']")

    search_button = (By.NAME, 'ACCEPT ALL')

class SearchResultPageLocators(object):
    pass
