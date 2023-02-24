import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

people = []
class microsoft:
    def micro_autom(self):
        s = Service("C:\Drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.google.co.in/")
        driver.maximize_window()
        driver.implicitly_wait(25)
        search = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        search.send_keys("microsoft teams login")
        search.send_keys(Keys.ENTER)

        driver.find_element(By.CSS_SELECTOR,"#rso > div:nth-child(1) > div.g.Ww4FFb.vt6azd.tF2Cxc > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a > h3").click()

        driver.find_element(By.XPATH,"//*[@id='highlight-oc1cec']/div/div[2]/div/div/div/div/div/div[2]/div[1]/a").click()

        new_tab = driver.window_handles[1]
        driver.switch_to.window(new_tab)

        driver.find_element(By.XPATH,"/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]").send_keys("kushal.s@sasken.com")
        driver.find_element(By.XPATH,"//*[@id='idSIButton9']").click()

        #To click profile
        #driver.find_element(By.XPATH,"//*[@id='personDropdown']/div/div/div/profile-picture/img").click()

        #To click status
        #driver.find_element(By.XPATH,"//*[@id='personal-skype-status-text']").click()

        #To click Appear Away
        #driver.find_element(By.XPATH,"/html/body/div[9]/ul/li[2]/button").click()

        #To set status message and send message
        #driver.find_element(By.CSS_SELECTOR,"#settings-dropdown-update-status-button").click()
        #driver.find_element(By.CSS_SELECTOR,"#setNoteBackButton").click()

        #New conversation
        #driver.find_element(By.XPATH,"//*[@id='new-post-button']").click()

        #Create new team or join
        '''driver.find_element(By.XPATH,"//*[@id='create_join_team_text']").click()
        driver.find_element(By.XPATH,"//*[@id='join-code-input']").send_keys("XYZ")
        a = driver.find_element(By.XPATH,"//*[@id='join-by-code-button']")
        a.click()'''
        #a.send_keys(Keys.ESCAPE)
        #alert = driver.switch_to.alert
        #alert.accept()
        #driver.find_element(By.CSS_SELECTOR, "#ngdialog6 > div.ngdialog-content > div > div.ts-modal-dialog-footer > div > button").send_keys(Keys.ENTER)
        a = driver.find_element(By.XPATH,"//*[@id='controlbox-input-group']")
        a.click()
        b = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/app-header-bar/div/power-bar/div/div/form/search-box/div/input")
        b.send_keys("m")
        b.send_keys(Keys.ENTER)

        '''c = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[4]/div/div/div/div[2]/div[2]/div[1]/div/ul/li/div/div/div/div/div[1]/div/img")
        c.click()'''
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/button[2]").click()

        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div[4]/div/div/div/div[1]/ul/li[3]/a").click()
        time.sleep(10)
m = microsoft()
m.micro_autom()