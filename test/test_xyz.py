import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
#from utilities.BaseClass import BaseClass

import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_One(BaseTest):

    def test_Url(self):
        title = self.driver.find_element(By.TAG_NAME, "strong").text
        time.sleep(4)
        assert (title == "XYZ Bank")


    # def test_customerLogin(self):
    #     self.find_element(By.XPATH,"//button[@ng-click='customer()']").click()
    #     self.find_element(By.XPATH,"//select[@name='userSelect']").click()
    #     a = ActionChains(self)
    #     a.key_down(Keys.ARROW_DOWN)
    #     a.click()
    #     a.perform()
    #     self.find_element(By.XPATH,"//button[@class='btn btn-default']").click()'''


# time.sleep(10)