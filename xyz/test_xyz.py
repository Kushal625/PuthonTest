from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest


@pytest.mark.usefixtures("init_driver")
class BaseClass:
    pass


class TestDemo(BaseClass):
    def test_Url(self):
        title = self.driver.find_element(By.CLASS_NAME, "mainHeading").text
        assert (title == "XYZ Bank")


class TestBankManager(BaseClass):

    def testManagerLogin(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Bank Manager Login']").click()
        add_cus_icon = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Customer']").text
        assert (add_cus_icon == "Add Customer")
        sleep(5)

    def test_addCustomer(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input").send_keys("Soham")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input").send_keys("Majumdar")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input").send_keys("0001")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/form/button").click()
        a = self.driver.switch_to.alert
        alert_text = a.text
        self.driver.switch_to.alert.accept()
        sub_str = 'Customer added successfully'
        assert sub_str in alert_text


class TestCustomer(BaseClass):

    def testcustomerlogin(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Customer Login')]").click()
        cust_name = Select(self.driver.find_element(By.ID, "userSelect"))
        cust_name.select_by_visible_text("Hermoine Granger")
        login = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/button").click()
        customer_page = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/strong").text
        assert ("Welcome Hermoine Granger !!")
        print(customer_page)

    def testdeposit(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[2]").click()
        amount = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[4]/div/form/div/input").send_keys("10000")
        enter = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/button").click()
        assert ("Deposit Successful")

    def testwithdrawl(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[3]").click()
        amount = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/div/input").send_keys("100")
        enter = self.driver.find_element(By.XPATH,  "/html/body/div/div/div[2]/div/div[4]/div/form/button").click()
        assert ("Transaction successful")


class TestTransaction(BaseClass):
    def testtransaction_1(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Customer Login']").click()
        dropdown = self.driver.find_element(By.ID, "userSelect")
        dropdown.click()
        dd = Select(dropdown)
        dd.select_by_visible_text('Hermoine Granger')
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Transactions'])[1]").click()
        self.driver.find_element(By.NAME, "start").click()
        self.driver.find_element(By.NAME, "start").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "end").send_keys(Keys.NUMPAD1)
        self.driver.find_element(By.NAME, "end").send_keys(Keys.ARROW_RIGHT)
        self.driver.find_element(By.NAME, "end").send_keys(Keys.NUMPAD1)
        table = self.driver.find_element(By.TAG_NAME, "tbody").text
        print("----Transactoin Details----")
        print()
        print(table)
        print()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Logout')]").click()
        sleep(1)

    def testtransaction_2(self):
        self.driver.find_element(By.XPATH, "/html/body").click()
        drop = self.driver.find_element(By.ID, "userSelect")
        drop.click()
        ddd = Select(drop)
        ddd.select_by_visible_text('Hermoine Granger')
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Transactions'])[1]").click()
        self.driver.find_element(By.NAME, "start").click()
        self.driver.find_element(By.NAME, "start").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "end").send_keys(Keys.NUMPAD7)
        self.driver.find_element(By.NAME, "end").send_keys(Keys.NUMPAD1)
        self.driver.find_element(By.NAME, "end").send_keys(Keys.ARROW_RIGHT)
        table1 = self.driver.find_element(By.TAG_NAME, "tbody").text
        print("----Transactoin Details in Oldest first order----")
        print()
        print(table1)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='>'])[1]").click()
        table2 = self.driver.find_element(By.TAG_NAME, "tbody").text
        print(table2)
