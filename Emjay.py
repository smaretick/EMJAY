# -*- coding: utf-8 -*-
#start BrowserStackLocal ./BrowserStackLocal --key 7UCbszm5qFWsYm1q3JZu
#mareticksm@gmail.com Sm110751$
#'browserstack.debug': 'true'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import unittest, time, re


desired_cap = {'browser': 'Chrome','browser_version': '80.0','os': 'OS X','os_version': 'High Sierra','project': 'EMJAY','browserstack.debug': 'true', 'resolution': '1600x1200'}

#desired_cap = {'browser': 'Firefox','browser_version': '62.0 beta','os': 'OS X','os_version': 'High #Sierra','project': 'TELETRAK','browserstack.debug': 'true'}

browser = webdriver.Remote(
    command_executor='http://scottmaretick2:MDKicy4nya2192zewKpz@hub.browserstack.com:80/wd/hub',
    desired_capabilities= desired_cap)


#runs with either Firefox or Chrome
#CHROME
options = webdriver.ChromeOptions()
options.add_argument('headless')
#options.add_argument('window-size= 1360 x 1400')
#browser = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver"),chrome_options=options;)
#browser = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver")
print(browser.get_window_size())
browser.set_window_size(1360, 1400)
print(browser.get_window_size())
#browser = webdriver.Firefox()  
#browser.maximize_window()
browser.get("https://www.emjaycons.com/")
#browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1.png');

print browser.title
#browser.window_handles
#browser.switch_to.active_element
#browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
browser.find_element_by_xpath("/html/body/nav/div/div/div[2]/ul/li[2]/div/a[1]").click() #ABOUT
time.sleep(10)
print browser.title
#browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2.png');

browser.find_element_by_xpath("/html/body/nav/div/div/div[2]/ul/li[3]/div/a[1]").click() #WHAT WE DO
time.sleep(10)
print browser.title
#browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot3.png');

browser.find_element_by_xpath("/html/body/nav/div/div/div[2]/ul/li[4]/a").click() #SERVICE DEPARTMENT
time.sleep(10)
print browser.title
#browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4.png');

browser.find_element_by_xpath("/html/body/nav/div/div/div[2]/ul/li[5]/div/a[1]").click() #PROJECTS
time.sleep(10)
print browser.title
#browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot5.png');

browser.find_element_by_xpath("/html/body/nav/div/div/div[2]/ul/li[6]/a").click()#CAREERS
time.sleep(10)
print browser.title
#browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot6.png');

browser.find_element_by_xpath("/html/body/nav/div/div/div[2]/ul/li[7]/a").click() #CONTACT
time.sleep(10)
print browser.title
#browser.save_screenshot('//Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot7.png');
browser.quit()
