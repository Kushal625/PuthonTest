from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from time import sleep
import pytest
import time


pytest.mark.usefixtures("init_dpytriver")
s = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

class BaseTest:
    pass


class TestUrl(BaseTest):
    def testUrl(self):
         title=self.driver.find_element(By.CLASS_NAME, "mainHeading").text
         time.sleep(3)
         assert (title == "XYZ Bank")


#class TestBankManager(BaseTest):

    #def testManagerLogin(self):
         #self.driver.find_element(By.XPATH, "//button[normalize-space()='Bank Manager Login']").click()
         #add_cus_icon = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Customer']").text
         #assert (add_cus_icon == "Add Customer")

    #def testAddCustomer(self):
        #self.driver.find_element(By.XPATH, "//button[normalize-space()='Bank Manager Login']").click()
        #self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Customer']").click()
        #self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("kavana")
        #self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("S J")
        #self.driver.find_element(By.XPATH, "//input[@placeholder='Post Code']").send_keys("98765")
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        #add_cus_popup = self.driver.switch_to_alert.text

        #assert (add_cus_popup == "Customer added successfully with customer id :6")



class TestCustomer(BaseTest):

    def testcustomerlogin(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/button").click()
        cust_name = Select(self.driver.find_element(By.ID, "userSelect"))
        cust_name.selct_by_visible_text("Harry Potter")
        login = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/button").click()
        customer_page = self.driver.find_element(By.ID, "/html/body/div/div/div[2]/div/div[1]/strong").text
        assert("Welcome Ron Weasly !!")


    def testdeposit(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[2]").click()
        amount = driver.find_element(By.XPATH,  "/html/body/div/div/div[2]/div/div[4]/div/form/div/input").send_keys("10000")
        enter = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/button").click()
        assert("Deposit Successful")

    def testwithdrawl(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[3]").click()
        amount = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/div/input").send_keys("100")
        enter = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/button").click()
        assert("Transaction successful")

    def testtransaction(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[1]").click()