import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def init_driver(request):
    baseURL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
    driver.get(baseURL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()