import unittest

from selenium import webdriver

from selenium.webdriver.common.keys import Keys



WAITING_TIME = 5





class login_page_test(unittest.TestCase):





    def test_login_fail(self):

        # super().__init__()

        self.user = "ecv"

        self.pwd = "12345"



        options = webdriver.ChromeOptions()

        options.add_argument("--start-maximized")



        self.driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)



        self.driver.get("http://www.facebook.com")

        assert "Facebook" in self.driver.title



        self.driver.implicitly_wait(WAITING_TIME)

        elem = self.driver.find_element_by_id("email")

        elem.send_keys(self.user)

        elem = self.driver.find_element_by_id("pass")



        elem.send_keys(self.pwd)



        self.driver.implicitly_wait(WAITING_TIME)



        elem.send_keys(Keys.RETURN)



        self.driver.implicitly_wait(WAITING_TIME)

        # assert "Log into Facebook" in driver.title

        self.assertEqual( "Log into Faebook" ,

                          self.driver.find_element_by_xpath('//*[@id="header_block"]/span').text)
#        self.driver.find_element_by_xpath("'//BUTTON[@id='u_0_u']").click()
#        assert "Facebook" in self.driver.title

        self.driver.close()




if __name__ == "__main__":

    unittest.main()