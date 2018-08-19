import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re


WAITING_TIME = 5

class Newuser_page_test(unittest.TestCase):


    def test_Newuser(self):
        self.url = 'https://www.facebook.com/'
        self.first_name = '9Sarah'
        self.last_name = 'Zhang'
        self.id = 'lihqzz@foxmail.com'
        self.password = 'Zwtlhq1019'

        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument("--start-maximized")

        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
        self.driver.get(self.url)
        assert "Facebook" in self.driver.title  #test if in the right page

        self.driver.implicitly_wait(WAITING_TIME)
        #self.first_name_input = self.driver.find_element_by_id("u_0_c")
        self.first_name_input = self.driver.find_element_by_xpath("//input[@name='firstname']")

        self.first_name_input.send_keys(self.first_name)
        #assert(re.match(r'(^[a-zA-Z]{2,19}$)',self.first_name))

        self.last_name_input = self.driver.find_element_by_xpath("//input[@name='lastname']")
        self.last_name_input.send_keys(self.last_name)

        self.id_input = self.driver.find_element_by_xpath("//input[@name='reg_email__']")
        self.id_input.send_keys(self.id)

        self.id_input = self.driver.find_element_by_xpath("//input[@name='reg_email_confirmation__']")
        self.id_input.send_keys(self.id)

        self.id_input = self.driver.find_element_by_xpath("//input[@name='reg_passwd__']")
        self.id_input.send_keys(self.password)



        self.driver.find_element_by_xpath('//button[@name="websubmit"]').click()

        self.assertRegex(self.first_name, r'(^[a-zA-Z]{2,19})', "Not allowed first name!!!")
        #try:
        #    assert self.first_name in r'(^[a-zA-Z]{2,19})'
        #except:
        #    print ("Not allowed first name!!!")


#       self.driver.implicitly_wait(WAITING_TIME)

#       self.assertIn (self.first_name , "r'*'")

    #define the rule to test new user first name, when enter, notify the error message
#   def test_first_name(self):
#       self.first_name_input = self.driver.find_elements_by_xpath("//INPUT[@id='u_0_n']").send_keys(self.first_name)
#        #match the rule to the input
#        #self.assertIn (,self.first_name_input.text)
#        pass

        #self.driver.close()







if __name__ == "__main__":

    unittest.main()