import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    s = Service(r"C:\Users\EE212981\PycharmProjects\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

