from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
from time import sleep

@pytest.mark.usefixtures("init_driver")

class BaseTest:
    pass

class Test_URL(BaseTest):
    def test_login(self):
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Customer Login')]").click()
        name = Select(self.driver.find_element(By.TAG_NAME,"select"))
        name.select_by_visible_text("Hermoine Granger")
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Login')]").click()

    def test_withdrawl_01(self): #To withdraw amount less then the balance
        self.driver.find_element(By.XPATH,"//button[@ng-class='btnClass3']").click()
        self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/form[1]/div[1]/input[1]").send_keys("1000")
        self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/form[1]/button[1]").click()

        success = self.driver.find_element(By.XPATH,"//span[contains(text(),'Transaction successful')]").text
        assert "Transaction successful" in success
        print(success)
        self.driver.refresh()

    def test_withdrawl_02(self): #To withdarw amount more then the balance
        self.driver.find_element(By.XPATH,"//button[@ng-class='btnClass3']").click()
        self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/form[1]/div[1]/input[1]").send_keys("10000")
        self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/form[1]/button[1]").click()

        fail = self.driver.find_element(By.XPATH,"//span[@class='error ng-binding']").text
        assert "Transaction Failed" in fail
        print(fail)
        self.driver.refresh()

    def test_withdrawl_03(self): #To withdraw amount in negative value
        self.driver.find_element(By.XPATH,"//button[@ng-class='btnClass3']").click()
        self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/form[1]/div[1]/input[1]").send_keys("-100")
        self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/form[1]/button[1]").click()

    def test_change_acc_01(self): #To change the account for same user and withdraw money
        all_acc = Select(self.driver.find_element(By.XPATH,"//select[@id='accountSelect']"))
        all_acc.select_by_visible_text("1002")
        print(self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[2]").text)
        self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/form[1]/div[1]/input[1]").clear()
        self.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/form[1]/div[1]/input[1]").send_keys("100")
        self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/form[1]/button[1]").click()

        fail = self.driver.find_element(By.XPATH,"//span[@class='error ng-binding']").text
        assert "Transaction Failed" in fail
        print(fail)
        sleep(2)
    
    def test_change_acc_02(self): #To change the account number to different value other than the provided number
        all_acc = Select(self.driver.find_element(By.XPATH,"//select[@id='accountSelect']"))
        all_acc.select_by_visible_text("1004")

    def test_logout(self): #Logout
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Logout')]").click()

        sleep(2)
