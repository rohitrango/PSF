from selenium import webdriver
import sys,requests

user = sys.argv[1]
pwd  = sys.argv[2]

from selenium.webdriver.common.keys import Keys
browser=webdriver.Firefox()

browser.get('https://www.facebook.com/')

elem = browser.find_element_by_id('email')
elem.send_keys(user)

elem = browser.find_element_by_id('pass')
elem.send_keys(pwd)
elem.submit()

browser.get("https://www.facebook.com/chinmay0301")
elem = browser.find_element_by_id("u_0_y")
elem.click()
elem = browser.find_element_by_class_name("_5rpu")
for i in range(27):
 elem.send_keys("#rg_test")
 elem.send_keys(Keys.RETURN)

    



