from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys

browser = webdriver.Firefox()
browser.get("http://gabrielecirulli.github.io/2048/")
sleep(1)
doc = browser.find_element_by_tag_name('body')

n = raw_input("Enter number of iterations/100.\n")
try:
	n = abs(int(n))
except:
	print "You should have entered an integer."
	sys.exit()

for i in range(100*n):
	doc.send_keys(Keys.UP)
	sleep(0.2)
	doc.send_keys(Keys.RIGHT)
	sleep(0.2)
	doc.send_keys(Keys.DOWN)
	sleep(0.2)
	doc.send_keys(Keys.LEFT)
	sleep(0.2)