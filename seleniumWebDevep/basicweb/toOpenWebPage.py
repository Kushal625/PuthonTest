from selenium import webdriver
class ChromeDriverWindows():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome(executable_path="C:\\Users\\EE212981\\PycharmProjects\\chromedriver.exe")
        driver.get(baseUrl)
c = ChromeDriverWindows()
c.test()