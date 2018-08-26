'''This program prints next 4 days temperature along with todays temperature

A practical use of BeautifulSoup'''

import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.timeanddate.com/weather/india/gurgaon/ext")
soup = BeautifulSoup(page.content, 'html.parser')
days = soup.find(id="wt-ext")
forecast_items = days.find_all(class_="c0") #for today
tomorrow = forecast_items[0]

forecast_items_1 = days.find_all(class_="c1") # for tomorrow
day_after_tomorrow = forecast_items_1[0]


test1 = tomorrow.get_text()
test2 = day_after_tomorrow.get_text()
test3 = forecast_items[1].get_text()
test4 = forecast_items_1[1].get_text()

#for today temperature

days_1 = soup.find(id="bk-focus")
forecast = days_1.find(class_='h2')

print("TODAY ",forecast.get_text())
print("DAY 1 ",test1)
print("DAY 2 ",test2)
print("DAY 3 ",test3)
print("DAY 4 ",test4)

#############################################################

'''this can be done with selenium'''
from selenium import webdriver
driver = webdriver.Chrome(r"C:\Users\visha\chromedriver")
driver.get('https://www.timeanddate.com/weather/india/gurgaon/ext')

test = '//*[@id="wt-ext"]/tbody/tr[1]/td[2]'
humd = '//*[@id="wt-ext"]/tbody/tr[1]/td[7]'
day = []
humidity = []

for i in range(1,6):
    daynew = test[0:-8]+str(i)+test[-7:-2]+test[-2:]
    day.append(driver.find_element_by_xpath(daynew).text)
for j in range(1,6):
    humdnew = humd[0:-8]+str(j)+humd[-7:-2]+humd[-2:]
    humidity.append(driver.find_element_by_xpath(humdnew).text)
ed = 1
for i in range(0,4):
    print('Day',ed,'Temp: ',day[i],'|','Humidity: ',humidity[i])
    ed = ed+1























