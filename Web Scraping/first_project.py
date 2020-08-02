from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = r"C:\src\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get(r'https://tutorial.math.lamar.edu/')

print(driver.title,'is online')
search = driver.find_element_by_id(r"gsc-i-id1")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)

# driver.close() #closes the tab
driver.quit() #closes the browser

