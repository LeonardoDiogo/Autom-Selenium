import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://demo.applitools.com/")

username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@type='checkbox']")

# is_displayed()
print(username.is_displayed())
assert username.is_displayed()

# is_enable()
print(username.is_enabled())
assert username.is_enabled()

# is_selected()
print(checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected()

time.sleep(2)
checkbox_remember_me.click()
time.sleep(2)

print(checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected()
