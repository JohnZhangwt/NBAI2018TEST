# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome().maximize_window()
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
#        self.driver.implicitly_wait(3)

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://192.168.88.216:8080/wallet/#/manage/main")
        driver.find_element_by_xpath("/html/body/app-root/app-manage/div/app-main/div/div[2]/ul/li[1]/button").click()
        #driver.find_element_by_xpath(
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
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Repeat Password'])[1]/following::button[1]").click()

        word = driver.find_element_by_id("mnemonic").text
        driver.find_element_by_xpath("//*[@id='popup']/form/div[3]/div[2]/button").click()
        driver.find_element_by_id("mnemonic").click()

        driver.find_element_by_id("mnemonic").clear()
        driver.find_element_by_id("mnemonic").send_keys(word)

        driver.find_element_by_xpath('//*[@id="popup"]/form/div[3]/div[2]/button').click()



#    def tearDown(self):
#        self.driver.quit()
#        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
