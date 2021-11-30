#dev-cndrw
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://popcat.click")

element = driver.find_element_by_id('app')
while True:
    element.click()
