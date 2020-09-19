import my_creds
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
def random_wait():
    time.sleep(random.random())
# setting up the options so as to prevent notification popups
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# chrome_options.add_argument('headless')
#instantiated the driver
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.minimize_window()


driver.get('http://www.facebook.com')
#waits till the onload event has fired

# assert 'Python' in driver.title


# pushing login data  https://www.edureka.co/community/3578/handle-notifications-python-with-selenium-chrome-webdriver
print("please wait, Loging in!")
elem = driver.find_element_by_id('email')
elem.clear()
elem.send_keys(my_creds.fb_uid)
random_wait()
elem = driver.find_element_by_id('pass')
elem.send_keys(my_creds.fb_pass)
elem.send_keys(Keys.RETURN)
random_wait()
# if nothing is found
assert not "No results found" in driver.page_source
print("logged in successfully!")
# friend_req_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[1]/div/a/div')
# friend_req_button.click()

driver.get("https://www.facebook.com/friends/requests/")
random_wait()
driver.find_element_by_xpath(r"//*[@id='FriendRequestMorePager']/div/a").click()
random_wait()
time.sleep(3)
print("friend requests acquired")
Friend_names = driver.find_elements_by_xpath(r"//div[@class='_6-_']/a")
print(len(Friend_names))
i = 0
with open('friend_requests.txt','w') as f:
    for friend in Friend_names:
        i += 1
        f.write(i,')',friend.get_attribute("title"))

driver.close()
driver.quit()
# we got all the friend requests
