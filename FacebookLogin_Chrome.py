from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re

WAITING_TIME = 5
url = 'https://www.facebook.com/'
user_name = 'lihqzz@foxmail.com'
password =  'Zwtlhq1019'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
#driver = webdriver.Chrome('./chromedriver.exe',chrome_options=chrome_options)
#driver = webdriver.Chrome('./chromedriver.exe')
driver.get(url)
driver.maximize_window()

driver.implicitly_wait(WAITING_TIME)
#exist_button = driver.find_element_by_partial_link_text("Log Into Existing Account").send_keys(Keys.RETURN)
driver.find_element_by_xpath("//INPUT[@id='email']").clear()
user_window = driver.find_element_by_xpath("//INPUT[@id='email']").send_keys(user_name)
pass_window = driver.find_element_by_xpath("//INPUT[@id='pass']").send_keys(password)
#driver.find_element_by_xpath("//INPUT[@id='u_0_2']").send_keys(Keys.RETURN)
#driver.find_element_by_xpath("//INPUT[@id='u_0_2']").click()
driver.find_element_by_id("loginbutton").click()


driver.implicitly_wait(WAITING_TIME)


#logout after login sucessfully
menu = driver.find_element_by_xpath("//DIV[@id='userNavigationLabel']")
menu.click()
logout = driver.find_element_by_partial_link_text("Log Out")
logout.click()
driver.find_element_by_xpath("//INPUT[@id='email']").clear()

driver.find_element_by_id("u_0_q").click()
driver.find_element_by_id("u_0_q").clear()
driver.find_element_by_id("u_0_q").send_keys("wentao")








