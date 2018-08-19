import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import allure



url = 'http://192.168.88.216:8080/wallet/#/manage/main'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

def test_addwallet():
    driver.find_element_by_xpath("/html/body/app-root/app-manage/div/app-main/div/div[2]/ul/li[1]/button").click()
    # driver.find_element_by_xpath(
    #    "(.//*[normalize-space(text()) and normalize-space(.)='Test2'])[1]/following::button[1]").click()
    driver.find_element_by_name("walletName").click()
    driver.find_element_by_name("walletName").clear()
    driver.find_element_by_name("walletName").send_keys("Test3")
    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("Test123")
    driver.find_element_by_name("rePassword").click()
    driver.find_element_by_name("rePassword").clear()
    driver.find_element_by_name("rePassword").send_keys("Test123")
    driver.find_element_by_xpath('//*[@id="popup"]/form/div[3]/div[2]/button').click()

    word = driver.find_element_by_xpath('//*[@id="popup"]/form/div[2]/div[2]').text
    print (word)
    driver.find_element_by_xpath("//*[@id='popup']/form/div[3]/div[2]/button").click()
    driver.find_element_by_id("mnemonic").clear()
    driver.find_element_by_id("mnemonic").send_keys(word)

    driver.find_element_by_xpath('//*[@id="popup"]/form/div[3]/div[2]/button').click()
#    NBaddress = driver.find_element('/html/body/app-root/app-manage/div/app-main/div/div[1]/div/div[2]/div[2]').content
#    print (str(NBaddress))

def test_importwallet():
    driver.find_element_by_xpath("/html/body/app-root/app-manage/div/app-main/div/div[2]/ul/li[2]/button").click()
    keystone = '{"version":3,"id":"9d8a5ee4-baa4-46b5-8c29-d58b5188e0ea","address":"ae793496baaee50d86d2d9bc4416bfd8c3160331","crypto":{"ciphertext":"7606d721c5bca765bce466e8245e6363df7f13d23002caaac270fe7bc1838ee6","cipherparams":{"iv":"856a5b7c4ad7b0496c98c30b8d1cd011"},"cipher":"aes-128-ctr","kdf":"scrypt","kdfparams":{"dklen":32,"salt":"a82faacc2db8afa696a2d6f6244e9a5c91e822db395d27e7b61299dc91bce7c9","n":8192,"r":8,"p":1},"mac":"2377b27877ceb1cf84dbbd8a1e2a243b2273cc0fe4d9e7946db97566904e1149"}}'
    driver.find_element_by_xpath('//*[@id="keystore"]').send_keys(keystone)
    # send key (ctrl -) twice to reduce the windows to 80%
    driver.switch_to.window(driver.window_handles[0])

    driver.find_element_by_xpath('//*[@id="popup"]/form/div[2]/div[2]/input').send_keys('Zwtlhq1019')
    driver.find_element_by_xpath('//*[@id="popup"]/form/div[3]/button').click()
