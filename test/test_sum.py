from selenium import webdriver
import time

baseUrl = "https://www.google.com"
driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
driver.get(baseUrl)
time.sleep(3)
