import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from code_ebay_unittesting.loginpage import Loginpage
from code_ebay_unittesting.Homepage import signin


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/aarviaditya/Desktop/Testing/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.ebay.ca")

        homepage = signin(driver)
        homepage.click_signin()

        login = Loginpage(driver)
        login.enter_username("parul34mittal@gmail.com")
        login.enter_password("testing789")
        login.click_login()

        homepage = signin(driver)
        homepage.add_cartitems()
        homepage.click_signout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/aarviaditya/Desktop/Testing/HTML_Python"),verbosity=2)

