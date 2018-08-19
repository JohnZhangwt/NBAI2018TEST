import pytest
from selenium import webdriver
import requests
import allure
from allure import AttachmentType




url = 'https://etherscan.io/'
driver = webdriver.Chrome()


def test_mainpage():
    mainpage = driver.get(url)
    assert 'Ethereum 'in driver.title
    assert 'Ethereum (ETH) BlockChain Explorer'== driver.title
    assert isinstance(driver.title,str)
    allure.attach('screenshot', driver.get_screenshot_as_png(),type=AttachmentType.PNG)


def test_homepage():
    homepage = requests.get(url)
    assert homepage.status_code == 200
    driver.save_screenshot('Ethereum website.png')


def test_homepage_error():
    homepage = requests.get(url)
    assert homepage.status_code == 300




