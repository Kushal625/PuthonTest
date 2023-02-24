from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest
import time
from Locators import locator

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
class Test_XYZ_Bank(BaseTest):
    def test_url(self):
        time.sleep(10)
        current_url=self.driver.current_url
        assert current_url=='https://www.globalsqa.com/angularJs-protractor/BankingProject/#/'

    def test_shortUrl(self):
        short_url = "https://rb.gy/x8hqzv"
        self.driver.get(short_url)
        cur_url = self.driver.current_url
        assert cur_url == "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    def test_title(self):
        assert self.driver.title == "XYZ Bank"

    def test_bank_manager_login(self):

        self.driver.find_element(By.XPATH,locator['Manager']).click()
        check=self.driver.find_element(By.XPATH,locator['Add_customer']).text
        assert check == "Add Customer"

    # ----- Taking Inputs for Add Customer -----
    @pytest.mark.parametrize(
                            "f_name, l_name, postcode",
                            [
                                ("","",""),
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
            # time.sleep(2)
            self.driver.find_element(By.XPATH,locator['l_name']).send_keys(l_name)
            # time.sleep(2)
            self.driver.find_element(By.XPATH,locator['post_code']).send_keys(postcode)
            # time.sleep(2)
            self.driver.find_element(By.XPATH,locator['cust_submit']).click()
            # time.sleep(2)
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

    # ----- Taking Inputs for Open Account -----
    @pytest.mark.parametrize(
                            "name, currency",
                            [
                                ('',"Rupee"),
                                ('Saurav Das',''),
                                ('Saurav Das',"Dollar"),
                                ('Saurav Das',"Pound")
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

    # ----- Taking Inputs for Customer Details -----
    @pytest.mark.parametrize(
                        "search",
                        [
                            ("Saurav"),
                            ("1001"),
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

    # ----- Taking Inputs for Delete Customer -----
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

    # ----- Taking Inputs for Customer Login -----
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
            
            sub_str2="Please open an account with us"
            success=self.driver.find_element(By.XPATH,locator['success']).text
            
            assert sub_str2 in success
            self.driver.find_element(By.XPATH,locator['home']).click()
        except:
            sub_str2="Welcome"
            assert sub_str2 in success
            self.driver.find_element(By.XPATH,locator['home']).click()

    # ----- Taking inputs for Print Account Details
    @pytest.mark.parametrize(
                        "name,Acc_index_no",
                        [
                            ('Hermoine Granger',1),
                            ('Saurav Das',1),
                            ("Harry Potter",2)

                        ]
                    )  
    def test_account(self,name,Acc_index_no):
        Your_Name=Select(self.driver.find_element(By.ID,locator['dropdown_id']))
        Your_Name.select_by_visible_text(name)
        self.driver.find_element(By.XPATH,locator['login']).click()

        Account=Select(self.driver.find_element(By.ID,locator['account']))
        Account.select_by_index(Acc_index_no)
        details=self.driver.find_element(By.XPATH,locator['details']).text
        self.driver.find_element(By.XPATH,locator['logout']).click()
        print(details)

    # ----- Taking inputs for Deposit -----   
    @pytest.mark.parametrize(
                        "name,acc_index_no,amount",
                        [
                            ("Hermoine Granger",2,"100000"),
                            ('Saurav Das',1,'50000'),
                            ("Saurav Das",1,'e'),
                            ('Harry Potter',1,'0')
                        ]
                    )  
    def test_deposit(self,name,acc_index_no,amount):

        Your_Name=Select(self.driver.find_element(By.ID,locator['dropdown_id']))
        Your_Name.select_by_visible_text(name)
        self.driver.find_element(By.XPATH,locator['login']).click()

        Account=Select(self.driver.find_element(By.ID,locator['acc-select']))
        Account.select_by_index(acc_index_no)
        self.driver.find_element(By.XPATH,locator['deposit']).click()
        self.driver.find_element(By.XPATH,  locator['amount']).send_keys(amount)
        self.driver.find_element(By.XPATH, locator['deposit/withdrawl']).click()

        D=(self.driver.find_element(By.XPATH,locator['deposit-success']).text)
        self.driver.find_element(By.XPATH,locator['logout']).click()
    
        assert D =="Deposit Successful"
            
    # ----- Taking Inputs for Withdrawl -----
    @pytest.mark.parametrize(
                        "name,acc_index_no,amount",
                        [
                            ("Hermoine Granger",2,"900"),
                            ("Harry Potter",1,'30'),
                            ("Saurav Das",1,"1000"),
                            ("soham",3,'100')
                        ]
                    )  
    def test_withdrawl(self,name,acc_index_no,amount):
        try:
            Your_Name=Select(self.driver.find_element(By.ID,locator['dropdown_id']))
            Your_Name.select_by_visible_text(name)
            self.driver.find_element(By.XPATH,locator['login']).click()
            Account=Select(self.driver.find_element(By.ID,locator['acc-select']))
            Account.select_by_index(acc_index_no)
            self.driver.find_element(By.XPATH, locator['withdrawl']).click()
            self.driver.find_element(By.XPATH, locator['amount']).send_keys(amount)
            self.driver.find_element(By.XPATH, locator['deposit/withdrawl']).click()
            self.driver.find_element(By.XPATH, locator['amount']).clear()

            assert self.driver.find_element(By.XPATH,locator['withdrawl-success']).text=="Transaction successful"
            self.driver.find_element(By.XPATH,locator['logout']).click()
        except:
            assert self.driver.find_element(By.XPATH,locator['withdrawl-success']).text=="Transaction Failed. You can not withdraw amount more than the balance."
            self.driver.find_element(By.XPATH,locator['logout']).click()

    # ----- Taking inputs for showing transactions -----
    @pytest.mark.parametrize(
                        "name,acc_no,start_date,start_month,end_date,end_month",
                        [
                            ('Hermoine Granger','1001',"15","04","20","04"),
                            ('Hermoine Granger','1001','01','01','01','01'),
                            ('Saurav Das','1017','','','',''),
                            ("Harry Potter",'1006',"01","01","05","07")

                        ]
                    )
    def test_transaction(self,name,acc_no,start_date,start_month,end_date,end_month):
                
            dropdown = Select(self.driver.find_element(By.ID, locator['dropdown_id']))
            dropdown.select_by_visible_text(name)
            self.driver.find_element(By.XPATH,locator['login']).click()
            Account=Select(self.driver.find_element(By.ID,locator['acc-select']))
            Account.select_by_visible_text(acc_no)
            self.driver.find_element(By.XPATH,locator['transaction']).click()
            if (self.driver.find_element(By.NAME, "start").is_displayed()):
                self.driver.find_element(By.NAME, "start").click()
                self.driver.find_element(By.NAME, "start").send_keys(start_date)
                self.driver.find_element(By.NAME, "start").send_keys(start_month)
                self.driver.find_element(By.NAME, "start").send_keys(Keys.TAB)
                self.driver.find_element(By.NAME, "end").send_keys(end_date)
                self.driver.find_element(By.NAME, "end").send_keys(end_month)
                self.driver.find_element(By.XPATH, locator["next_page"]).click()
                table1 = self.driver.find_element(By.TAG_NAME, "tbody").text
                self.driver.find_element(By.XPATH,locator['logout']).click()

                print("----Transactoin Details in Oldest first order----")
                print(table1)
            else:
                print(self.driver.find_element(By.TAG_NAME, "tbody").text)
                self.driver.find_element(By.XPATH,locator['logout']).click()
    # ----- Taking inputs for reset the transaction -----
    @pytest.mark.parametrize(
                        "name,acc_no",
                        [
                            ("Saurav Das","1016"),
                            ("Harry Potter",'1004'),
                            ("Soham Majumdar","1016")

                        ]
                    ) 
    def test_reset(self,name,acc_no):
        Your_Name=Select(self.driver.find_element(By.ID,locator['dropdown_id']))
        Your_Name.select_by_visible_text(name)
        self.driver.find_element(By.XPATH,locator['login']).click()
        Account=Select(self.driver.find_element(By.ID,locator['acc-select']))
        Account.select_by_visible_text(acc_no)
        self.driver.find_element(By.XPATH, locator['transaction']).click()
        if (self.driver.find_element(By.NAME, "start").is_displayed()):
            self.driver.find_element(By.XPATH,locator['reset']).click()
            reset=self.driver.find_element(By.XPATH,locator['transaction-table']).text
            self.driver.find_element(By.XPATH,locator['logout']).click()
            assert reset=="Date-Time Amount Transaction Type"
        else:
            self.driver.find_element(By.XPATH,locator['logout']).click()
    # ----- Taking inputs for checking Back -----
    @pytest.mark.parametrize(
                        "name,acc_no",
                        [
                            ("Harry Potter",'1004')
                        ]
                    ) 
    def test_back(self,name,acc_no):
        Your_Name=Select(self.driver.find_element(By.ID,locator['dropdown_id']))
        Your_Name.select_by_visible_text(name)
        self.driver.find_element(By.XPATH,locator['login']).click()
        Account=Select(self.driver.find_element(By.ID,locator['acc-select']))
        Account.select_by_visible_text(acc_no)
        self.driver.find_element(By.XPATH, locator['transaction']).click()
        self.driver.find_element(By.XPATH,locator['back']).click()
        assert self.driver.find_element(By.XPATH, locator['transaction']).text=='Transactions'
        self.driver.find_element(By.XPATH,locator['logout']).click()
    
    # ----- Taking inputs for checking Logout -----
    @pytest.mark.parametrize(
                        "name",
                        [
                            ("Hermoine Granger")
                        ]
                    )
    def test_logout(self,name):
        Your_Name=Select(self.driver.find_element(By.ID,locator['dropdown_id']))
        Your_Name.select_by_visible_text(name)
        self.driver.find_element(By.XPATH,locator['login']).click()
        self.driver.find_element(By.XPATH,locator['logout']).click()
        assert self.driver.find_element(By.XPATH,locator['your-name']).text=='Your Name :'
