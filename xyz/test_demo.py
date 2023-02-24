from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest
from Locators import locator

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_URL(BaseTest):
    # def test_url(self):
    #     title=self.driver.find_element(By.CLASS_NAME,locator['url_xpath']).text
    #     assert title=="XYZ Bank"

    # def test_curUrl(self):
    #     cur_url = self.driver.current_url
    #     assert cur_url=="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        
    # def test_shortUrl(self):
    #     short_url = "https://rb.gy/x8hqzv"
    #     self.driver.get(short_url)
    #     cur_url = self.driver.current_url
    #     assert cur_url == "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

# class Test_BankManager(BaseTest):

    def test_bank_manager_login(self):

        self.driver.find_element(By.XPATH,locator['Manager']).click()
        check=self.driver.find_element(By.XPATH,locator['Add_customer']).text
        assert check == "Add Customer"

    @pytest.mark.parametrize(
                            "f_name, l_name, postcode",
                            [
                                ("Saurav","Das","212770"),
                                ("Saurav","Das","212770"),
                                ("Rick",'Majumdar','212888'),
                                ("123",'789','122100'),
                                ("@$&","#*+","EE1122")
                            ]
                        )
    def test_addCustomer(self,f_name,l_name,postcode):
        try:
            self.driver.find_element(By.XPATH,locator['Add_customer']).click()
            self.driver.find_element(By.XPATH,locator['f_name']).send_keys(f_name)
            self.driver.find_element(By.XPATH,locator['l_name']).send_keys(l_name)
            self.driver.find_element(By.XPATH,locator['post_code']).send_keys(postcode)
            self.driver.find_element(By.XPATH,locator['cust_submit']).click()

            a=self.driver.switch_to.alert
            alert_text = a.text
            self.driver.switch_to.alert.accept()
            
            self.driver.find_element(By.XPATH,locator['f_name']).clear()
            self.driver.find_element(By.XPATH,locator['l_name']).clear()
            self.driver.find_element(By.XPATH,locator['post_code']).clear()

            sub_str='Customer added successfully'
            assert sub_str in alert_text
        except:
            sub_str3="Please check the details."
            assert sub_str3 in alert_text

    @pytest.mark.parametrize(
                            "name, currency",
                            [
                                ('Saurav Das',"Rupee"),
                                ('Saurav Das','Dollar'),
                                ('123 789',"Dollar"),
                                ('@$& #*+',"Pound")
                            ]
                        )
    def test_openAccount(self,name,currency):
        self.driver.find_element(By.XPATH,locator['open_acc']).click()
        customer=Select(self.driver.find_element(By.ID,locator['dropdown_id']))
        customer.select_by_visible_text(name)
        Currency=Select(self.driver.find_element(By.ID,locator['curr_id']))
        Currency.select_by_visible_text(currency)
        self.driver.find_element(By.XPATH,locator['acc_submit']).click()

        a=self.driver.switch_to.alert
        alert_text = a.text
        self.driver.switch_to.alert.accept()

        sub_str1="Account created successfully with account Number"
        assert sub_str1 in alert_text

    @pytest.mark.parametrize(
                        "search",
                        [
                            ("Saurav"),
                            ("1018"),
                            ("Majumdar"),
                            ('EE1122'),
                            ('Ribhu')
                        ]
                    )
    def test_customer(self,search):
        self.driver.find_element(By.XPATH,locator['customer']).click()
        self.driver.find_element(By.XPATH,locator['search']).send_keys(search)
        Table=self.driver.find_element(By.XPATH,locator['cust_table']).text
        self.driver.find_element(By.XPATH,locator['search']).clear()
        
        assert search in Table
    
    @pytest.mark.parametrize(
                        "remove",
                        [
                            ("Ron"),
                            ("789"),
                            ('EE1122')
                        ]
                    )
    def test_remove(self,remove):

        self.driver.find_element(By.XPATH,locator['search']).send_keys(remove)
        self.driver.find_element(By.XPATH,locator['delete']).click()
        self.driver.refresh()
        Table=self.driver.find_element(By.XPATH,locator['cust_table']).text

        assert remove not in Table

    def test_home(self):

        self.driver.find_element(By.XPATH,locator['home']).click()
        assert (self.driver.find_element(By.XPATH,locator['customer_login']).text)=='Customer Login'
    
    @pytest.mark.parametrize(
                        "name",
                        [
                            ("Hermoine Granger"),
                            ("Saurav Das"),
                            ("Rick Majumdar"),
                            ("123 789")
                        ]
                    )
    def test_customer_login(self,name):
        try:
            self.driver.find_element(By.XPATH,locator['customer_login']).click()
            Your_Name=Select(self.driver.find_element(By.ID,locator['dropdown_id']))
            Your_Name.select_by_visible_text(name)
            self.driver.find_element(By.XPATH,locator['login']).click()
            
            sub_str2="Welcome"
            success=self.driver.find_element(By.XPATH,locator['success']).text
            
            assert sub_str2 in success
            self.driver.find_element(By.XPATH,locator['home']).click()
        except:
            sub_str2="Please open an account with us"
            assert sub_str2 in success

    @pytest.mark.parametrize(
                        "name,Acc_no",
                        [
                            ('Hermoine Granger',"1001"),
                            ('Saurav Das','1016'),
                            ("@$& #*+","1019")

                        ]
                    )  
    def test_account(self,name,Acc_no):

        Your_Name=Select(self.driver.find_element(By.ID,locator['dropdown_id']))
        Your_Name.select_by_visible_text(name)
        self.driver.find_element(By.XPATH,locator['login']).click()

        Account=Select(self.driver.find_element(By.ID,locator['account']))
        Account.select_by_visible_text(Acc_no)
        print(self.driver.find_element(By.XPATH,locator['details']).text)

        self.driver.find_element(By.XPATH,locator['logout']).click()

    # ----- Taking inputs for Deposit -----   
    @pytest.mark.parametrize(
                        "name,acc_no,amount",
                        [
                            ("Hermoine Granger","1002","100000"),
                            # ("Saurav Das","1017","50000"),
                            # ('Harry Potter','1016','10000')
                        ]
                    )  
    def test_deposit(self,name,acc_no,amount):

        Your_Name=Select(self.driver.find_element(By.ID,locator['dropdown_id']))
        Your_Name.select_by_visible_text(name)
        self.driver.find_element(By.XPATH,locator['login']).click()

        Account=Select(self.driver.find_element(By.ID,locator['acc-select']))
        Account.select_by_visible_text(acc_no)
        self.driver.find_element(By.XPATH,locator['deposit']).click()
        self.driver.find_element(By.XPATH,  locator['amount']).send_keys(amount)
        self.driver.find_element(By.XPATH, locator['deposit/withdrawl']).click()

        D=(self.driver.find_element(By.XPATH,locator['deposit-success']).text)
        self.driver.find_element(By.XPATH,locator['logout']).click()
    
        assert D =="Deposit Successful"
            
            # self.driver.find_element(By.XPATH,locator['logout']).click()

    # ----- Taking Inputs for Withdrawl -----
    @pytest.mark.parametrize(
                        "name,acc_no,amount",
                        [
                            ("Hermoine Granger","1002","900"),
                            ("Harry Potter","1006",'30'),
                            ("Saurav Das",'1017',"1000"),
                            ("soham",'1020','100')
                        ]
                    )  
    def test_withdrawl(self,name,acc_no,amount):
        try:
            Your_Name=Select(self.driver.find_element(By.ID,locator['dropdown_id']))
            Your_Name.select_by_visible_text(name)
            self.driver.find_element(By.XPATH,locator['login']).click()
            Account=Select(self.driver.find_element(By.ID,locator['acc-select']))
            Account.select_by_visible_text(acc_no)
            self.driver.find_element(By.XPATH, locator['withdrawl']).click()
            self.driver.find_element(By.XPATH, locator['amount']).send_keys(amount)
            self.driver.find_element(By.XPATH, locator['deposit/withdrawl']).click()
            self.driver.find_element(By.XPATH, locator['amount']).clear()

            assert self.driver.find_element(By.XPATH,locator['withdrawl-success']).text=="Transaction successful"
            self.driver.find_element(By.XPATH,locator['logout']).click()
        except:
            assert self.driver.find_element(By.XPATH,locator['withdrawl-success']).text=="Transaction Failed. You can not withdraw amount more than the balance."
            self.driver.find_element(By.XPATH,locator['logout']).click()
