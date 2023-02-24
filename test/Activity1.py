#Activity-1: Get the maximum holiday months for a given year other than yearly vacation(December)

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from collections import Counter

#To login to iken holiday list
s = Service(r"C:\Users\EE212981\PycharmProjects\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://kenpoint.sasken.com/hr/intcom/SaskenHolidayList/Holiday%20List%202023.aspx")
driver.maximize_window()
driver.implicitly_wait(15)

#List of holidays
page = driver.find_element(By.XPATH,"//*[@id='layoutsTable']/tbody/tr/td/div/div/div/table/tbody").text.split('\n')
print(page)
#To select holiday list of Bangalore location
holidays = page[1:11]
#print(holidays)


#To remove December from the list and print maximum holidays in a year
month = []
for i in range(len(holidays)):
    if(holidays[i].split()[0]) != 'December':
        month.append(holidays[i].split()[0])
holiday = Counter(month)
highestholiday = holiday.most_common(1)

#Output
print("Highest hoilday of a month in the given year is:" + highestholiday[0][0])
print(highestholiday[0][1])

time.sleep(10)