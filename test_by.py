from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://netology.ru/"

try:
    driver = webdriver.Chrome()
    driver.get(url)
    name = driver.find_element(By.CSS_SELECTOR, 'input.styles_input__OaA3T[type="text"]')
    name.send_keys('Петр')
    number = driver.find_element(By.CSS_SELECTOR, 'input.styles_input__OaA3T[type="tel"]')
    number.send_keys('89126887257')
    email = driver.find_element(By.CSS_SELECTOR, 'input.styles_input__OaA3T[type="email"]')
    email.send_keys('petr@mail.ru')
    button = driver.find_element(By.CSS_SELECTOR, 'button.styles_button__3chpH')
    button.click()
    time.sleep(10)
finally:

    driver.close()