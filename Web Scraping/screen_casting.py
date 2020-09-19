from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.google.com')

element = driver.find_element_by_xpath('/html/body/div')

actionChains = ActionChains(driver)

actionChains.context_click(element).perform()
