import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


s = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.implicitly_wait(25)
class Sasken():    def fun1(self):          s = Service(r"C:\Users\EE212950\chromedriver.exe")          driver = webdriver.Chrome(service=s)          driver.get("https://www.saucedemo.com/")          driver.maximize_window()          driver.implicitly_wait(10)          driver.find_element(By.ID,"user-name").send_keys("standard_user")          driver.find_element(By.ID,"password").send_keys("secret_sauce")          driver.find_element(By.ID,"login-button").click()          time.sleep(12)          driver.find_element(By.ID,"react-burger-menu-btn").click()          time.sleep(6)          b = driver.find_element(By.ID,"about_sidebar_link").click()          time.sleep(5)          clickable = driver.find_element(By.CSS_SELECTOR,"header.nav.is-secondary:nth-child(1) div.container nav.nav-container ul.nav-navigation-list li.nav-menu-list-container ul.nav-menu-list:nth-child(2) li.nav-menu-list-item:nth-child(5) div.nav-menu div.nav-menu-main-link.has-sub-menu > a.link")          time.sleep(5)          a = clickable.is_displayed()          #if a :          print("passed")          print(a)          clickble1 = b.find_element(By.CSS_SELECTOR,"header.nav.is-secondary:nth-child(1) div.container nav.nav-container ul.nav-navigation-list li.nav-menu-list-container ul.nav-menu-list:nth-child(2) li.nav-menu-list-item:nth-child(1) div.nav-menu div.nav-menu-main-link.has-sub-menu > a.link")          clickble1.click()          #          print("pass")          print(clickble1)ff=Sasken()ff.fun1()