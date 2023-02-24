import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    driver.implicitly_wait(15)
    request.cls.driver = driver
    yield
    driver.close()