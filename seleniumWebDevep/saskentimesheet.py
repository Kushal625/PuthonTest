import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


s = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://sdp.sasken.com/")
driver.maximize_window()

     # for login ID
a = driver.find_element(By.XPATH, "//*[@id='username']")
a.send_keys("ee212471")

     # for login password
b = driver.find_element(By.XPATH, "//*[@id='password']")
b.send_keys("212471@sas")

c = driver.find_element(By.XPATH, "//*[@id='login-submit']")
c.click()

d = driver.find_element(By.XPATH, "//*[@id='top-menu']/ul/li[4]/a")
d.click()

project = driver.find_element(By.XPATH, "//*[@id='edit_tr']/td[4]/input[4]")
project.send_keys("8.5")
project.click()

comment = driver.find_element(By.XPATH,"//*[@id='edit_tr']/td[5]/button/img")
comment.click()

commentpage = driver.find_element(By.XPATH,"//*[@id='comment-body']")
commentpage.send_keys("timesheet automation using python selenium")

time.sleep(10)

addcomment = driver.find_element(By.XPATH,"//*[@id='commentModal']/div/div/div[3]/button/p")
addcomment.click()

time.sleep(10)