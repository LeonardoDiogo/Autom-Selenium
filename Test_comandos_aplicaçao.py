from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://saucedemo.com/")

print("o titulo da pagina é:", browser.title)

print("a URL da pagina é:", browser.current_url)

print("o codigo fonte da pagina é:", browser.page_source)
