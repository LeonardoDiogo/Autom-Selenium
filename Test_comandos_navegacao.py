import time

from selenium import webdriver

browser = webdriver.Chrome()

browser.maximize_window()

browser.get("https://google.com")

browser.refresh()

browser.get("https://www.saucedemo.com/")

time.sleep(2)

browser.back()
time.sleep(3)

browser.forward()
time.sleep(3)

browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(3)

browser.quit()
