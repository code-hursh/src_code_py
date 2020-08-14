# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

def random_wait(d = 0):
    if d == 0:
        time.sleep(random.randint(1,3))
    else:
        time.sleep(d)
class Chrome:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications":2}
        chrome_options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(chrome_options = chrome_options)

    def fxpath(self,path):
        return self.driver.find_element_by_xpath(path)

    def fxpaths(self,path):
        return self.driver.find_elements_by_xpath(path)

    def fid(self,path):
        return self.driver.find_element_by_id(path)

    def login(self,_id,id_path,password,pass_path,button = None, temp = True, temp_path = None):
        self.id = _id
        _id = self.fxpath(id_path)
        _id.send_keys(self.id)
        _id.send_keys(Keys.RETURN)
        self.passw = password
        while True:
            try:
                password = self.fxpath(pass_path)
                random_wait()
                password.send_keys(self.passw)
                break
            except:
                continue
        random_wait()
        password.send_keys(Keys.RETURN)
        # if not button is None:
        #     self.fxpath(button).click()
        random_wait()
        if "stay signed in" in self.driver.page_source.casefold():
            self.fxpath(temp_path).click()

    def refresh(self):
        self.driver.refresh()
