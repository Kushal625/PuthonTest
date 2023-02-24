import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(r"C:\Users\EE212981\PycharmProjects\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://jam.sasken.com/home")
time.sleep(10)