from selenium import webdriver
import pytest

@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    if request.param =="chrome":
        web_driver=webdriver.Chrome()
    web_driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    web_driver.implicitly_wait(5)
    web_driver.maximize_window()
    request.cls.driver=web_driver

    yield
    web_driver.close()
    web_driver.quit()