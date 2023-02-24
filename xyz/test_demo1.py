from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_URL(BaseTest):
    def test_url(self):
        title = self.driver.find_element(By.XPATH,"//strong[contains(text(),'XYZ Bank')]").text
        assert title == "XYZ Bank"

    def test_curUrl(self):
        curUrl = self.driver.current_url
        assert curUrl == "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    def test_bankManagerLogin(self):
        self.driver.find_element(By.CSS_SELECTOR,"body.ng-scope:nth-child(2) div.ng-scope:nth-child(1) div.container-fluid.ng-scope div.ng-scope div.ng-scope div.borderM.box.padT20 div.center:nth-child(3) > button.btn.btn-primary.btn-lg").click()

    def test_addCust(self):
        text1 = self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").text
        assert text1 == "Add Customer"

        self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys("Kushal")
        self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/input[1]").send_keys("S")
        self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/input[1]").send_keys(560083)
        self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/button[1]").click()

        a=self.driver.switch_to.alert
        alert_text = a.text
        self.driver.switch_to.alert.accept()
        assert "Customer added successfully with customer" in alert_text

    def test_openAcc(self):
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/button[2]").click()
        customer=Select(self.driver.find_element(By.ID,"userSelect"))
        customer.select_by_visible_text("Kushal S")
        Currency=Select(self.driver.find_element(By.ID,"currency"))
        Currency.select_by_visible_text("Rupee")
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div/div/form/button").click()

        popUp=self.driver.switch_to.alert
        alert_text = popUp.text
        self.driver.switch_to.alert.accept()
        assert "Account created successfully with account Number" in alert_text

    def test_delCustomers(self):
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/button[3]").click()
        self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/input[1]").send_keys("kus")
        table = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[2]/div/div/table").text
        print(table)
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Delete')]").click()

    def test_home(self):
        home = self.driver.find_element(By.XPATH,"//button[contains(text(),'Home')]").text
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Home')]").click()
        assert home == "Home"
        print(home)
        


        
        sleep(2)