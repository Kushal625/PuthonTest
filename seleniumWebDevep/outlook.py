import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class outlook:
    def outlook_auto(self):
        s = Service(r"C:\Users\EE212981\PycharmProjects\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.google.co.in/")
        driver.maximize_window()
        driver.implicitly_wait(15)
        a = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        a.send_keys("outlook")
        a.send_keys(Keys.ENTER)
        b = driver.find_element(By.XPATH,"//*[@id='rso']/div[2]/div/div/div[1]/div/a/h3")
        b.click()

        driver.find_element(By.XPATH,"//*[@id='i0116']").send_keys("kushal.s@sasken.com")
        driver.find_element(By.XPATH,"//*[@id='idSIButton9']").click()

        d = driver.find_element(By.XPATH,"//*[@id='innerRibbonContainer']/div[1]/div/div/div/div[2]/div/div/span/button[2]")
        d.click()

        e = driver.find_element(By.XPATH,"//*[@id='Ribbon-588Dropdown']/div/ul/li/div/ul/li[1]/button/div/span")
        e.click()

        #To login to outlook
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[1]/div[1]/div/div[4]/div/div/div[1]").click()
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[1]/div[1]/div/div[4]/div/div/div[1]").send_keys("kushal.s@sasken.com")

        driver.find_element(By.XPATH,"//*[@id='FloatingSuggestionsItemId-0']/div/button[1]/span/div/div/div/div[2]/span[2]").click()

        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/input").click()
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/input").send_keys("Automation")

        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[2]/div/div/div").click()
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[2]/div/div/div").send_keys("automation testing using python")
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[2]/div/div/div").send_keys(Keys.ENTER)

        #To select the Font style of text
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div/input").click()
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div/input").send_keys("times new roman")
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div/input").send_keys(Keys.ENTER)

        #To select the Font size of text
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[3]/div[2]/div/div[3]/div/input").click()
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[3]/div[2]/div/div[3]/div/input").send_keys("18")
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[3]/div[2]/div/div[3]/div/input").send_keys(Keys.ENTER)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[2]/div/div/div").send_keys("its working")
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div/div/div/div[2]/div/div/div").send_keys(Keys.ENTER)

        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[1]/div/span/div/div[1]/div[1]/div/div[1]/div/div/div/span/div/div/div/div[5]/div/button/span/span/span").click()

        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[1]/div/span/div/div[2]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[5]/div/button/span/span[1]/span").click()

        driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/button[1]/span/span/span").click()

        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[1]/div/span/div/div[1]/div[1]/div/div[1]/div/div/div/span/div/div/div/div[7]/div/button/span/span/span").click()

        time.sleep(10)



c = outlook()
c.outlook_auto()