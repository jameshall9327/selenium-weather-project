from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.weather.gov/")
inputElement = driver.find_element_by_id("inputstring")
inputElement.click()
inputElement.send_keys('43040')
time.sleep(1)
auto_complete = driver.find_element_by_class_name('autocomplete-suggestion')
auto_complete.click()
