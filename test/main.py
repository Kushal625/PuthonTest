import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    driver.maximize_window()

def test_Url(self):
    title = self.driver.find_element(By.XPATH,"//strong[@class='mainHeading']").text
    time.sleep(3)
    assert (title == "XYZ Bank")