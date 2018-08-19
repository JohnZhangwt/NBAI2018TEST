import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import allure





url = 'http://192.168.88.216:8080/trogarzo'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

allure.step('test_mainpage')
def test_mainpage():
    driver.get(url)
    assert 'TROGARZO 'in driver.title
    print (driver.title)
    assert 'Now Approved: TROGARZO (ibalizumab-uiyk) Injection'== driver.title
    assert isinstance(driver.title,str)

allure.step('test_homepage')
def test_homepage():
    homepage = requests.get(url)
    assert homepage.status_code == 200
    driver.save_screenshot('Trogarzo website.png')

allure.step('test_safety')
def test_safety():
#    driver.get(url)
    driver.find_element_by_xpath('// *[ @ id = "isi"]').click()
    assert 'IMPORTANT SAFETY INFORMATION' in driver.page_source

allure.step('test_prescribing')
def test_prescribing():
#    driver.get(url)
    driver.find_element_by_xpath('//*[@id="mItems"]/li[2]/a').click()
    assert 'TrogarzoPrescribingInformation.pdf' in driver.page_source
    driver.switch_to.window(driver.window_handles[0])

allure.step('test_patient')
def test_patient():
#    driver.get(url)
    driver.find_element_by_xpath('//*[@id="mItems"]/li[3]/a').click()
    assert 'TrogarzoPatientInformation.pdf' in driver.page_source
    driver.switch_to.window(driver.window_handles[0])

allure.step('test_enrollment')
def test_enrollment():
#    driver.get(url)
    driver.find_element_by_xpath('// *[ @ id = "mItems"] / li[5] / a').click()
    assert 'TROGARZO_Enrollment_Form_fillable.pdf' in driver.page_source
    driver.switch_to.window(driver.window_handles[0])

allure.step('test_registerupdat')
def test_registerupdat():
#    driver.get(url)
    driver.find_element_by_xpath('// *[ @ id = "mItems"] / li[4] / a').click()
    driver.find_element_by_xpath('//*[@id="firstName"]').send_keys("Test123")
    driver.find_element_by_xpath('//*[@id="lastName"]').send_keys("Zhao")
    driver.find_element_by_xpath('//*[@id="email"]').send_keys("lihqzz@foxmail.com")
    driver.find_element_by_xpath('//*[@id="address"]').send_keys("4500 Linton")
    driver.find_element_by_xpath('//*[@id="state"]').send_keys("California")
    driver.find_element_by_xpath('//*[@id="city"]').send_keys("California")
    driver.find_element_by_xpath('// *[ @ id = "zipcode"]').send_keys("45000")
    driver.find_element_by_xpath('// *[ @ id = "telephone"]').send_keys("209-200-6296")
    driver.save_screenshot('Before Register.png')
    driver.find_element_by_xpath('//*[@id="submitForm"]').send_keys(Keys.ENTER)
    assert 'Thank you for registering.' in driver.page_source













