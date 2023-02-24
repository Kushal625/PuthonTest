import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("kushal s")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("aeiouaeiou")
        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='continents']"))
        time.sleep(10)