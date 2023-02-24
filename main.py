import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Search_char:
   def check_occerance(self):
        s = Service(r"C:\Users\EE212981\PycharmProjects\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.google.co.in/")
        driver.maximize_window()


        a = driver.find_element(By.XPATH,"//input[@class='gLFyf']")
        a.send_keys("Online gdb python compiler")
        a.send_keys(Keys.ENTER)
        d=driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[1]/div/a/h3")
        d.click()
        driver.find_element(By.XPATH,"//*[@id='editor_1']/div[2]/div").click()
        a = ActionChains(driver)
        a.key_down(Keys.CONTROL).send_keys("a")
        a.key_up(Keys.CONTROL)
        a.key_down(Keys.CONTROL).send_keys("x")
        a.key_up(Keys.CONTROL)
        a.send_keys("s=input()")
        a.key_down(Keys.ENTER)
        a.key_up(Keys.ENTER)
        a.send_keys("n=input()")
        a.key_down(Keys.ENTER)
        a.key_up(Keys.ENTER)
        a.send_keys("count=0")
        a.key_down(Keys.ENTER)
        a.key_up(Keys.ENTER)
        a.send_keys("for i in range(len(s)):")
        a.key_down(Keys.ENTER)
        a.key_up(Keys.ENTER)
        a.send_keys("if (s[i] == n):")
        a.key_down(Keys.ENTER)
        a.key_up(Keys.ENTER)
        a.send_keys("count+=1 ")
        a.key_down(Keys.ENTER)
        a.key_up(Keys.ENTER)
        a.key_down(Keys.BACK_SPACE)
        a.key_down(Keys.BACK_SPACE)
        a.send_keys("print(count)")
        a.perform()

        driver.find_element(By.ID,"input_method_text").click()
        i=driver.find_element(By.XPATH,"//*[@id='stdinput']")
        i.send_keys("Hello world")
        i.send_keys(Keys.ENTER)
        i.send_keys("l")
        driver.find_element(By.XPATH,"//*[@id='control-btn-run']").click()
        time.sleep(10)
        print(driver.find_element(By.XPATH,"//*[@id='stdout-container']").text)



S = Search_char() 
S.check_occerance()