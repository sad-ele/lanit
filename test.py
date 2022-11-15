from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://atha.yoga/')
time.sleep(2)
signup_button = browser.find_element(By.LINK_TEXT, "Регистрация")
signup_button.click()
time.sleep(2)
browser.close()
