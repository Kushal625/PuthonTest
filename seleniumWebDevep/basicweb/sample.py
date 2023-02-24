from selenium import webdriver
class ChromeDriverWindows():

    def test(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\EE212981\\PycharmProjects\\chromedriver.exe")
        driver.get("https://www.google.com")
c = ChromeDriverWindows()
c.test()