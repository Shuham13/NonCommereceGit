import time
import pytest

from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login import LoginPage
from utilites.ReadProperties import ReadConfig
from utilites.logger import LogGenerator

class Test_Login_Params:
    Url = ReadConfig.URL()
    username = ReadConfig.Email()
    password = ReadConfig.Password()
    log = LogGenerator.loggen()

    def test_login_params(self, setup, getDataforlogin):
        self.driver = setup
        self.log.info("test_login_params is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(getDataforlogin[0])
        self.log.info("Entering username-->" + getDataforlogin[0])
        self.lp.Enter_Password(getDataforlogin[1])
        self.log.info("Entering password-->" + getDataforlogin[1])
        self.lp.Click_Login()
        self.log.info("Click on login button")

        if self.driver.title == "Dashboard / nopCommerce administration":
            if getDataforlogin[2] == "Pass":
                self.driver.save_screenshot("C:\\Users\\shubham pate\\PycharmProjects\\NonCommerence 16 may "
                                            "23\\NonCommerence\\Screenshots\\test_login_002-pass.png")
                self.lp.Click_Logout()
                self.log.info("Click on logout button")
                self.log.info("test_login_002 is Passed")
                assert True
            else:
                self.log.info("test_login_002 is Failed")
                self.driver.save_screenshot(
                    "C:\\Users\\shubham pate\\PycharmProjects\\NonCommerence 16 may "
                    "23\\NonCommerence\\Screenshots\\test_login_002-fail.png")
                assert False
        else:
            if getDataforlogin[2] == "Fail":
                assert True
            else:
                self.log.info("test_login_002 is Failed")
                self.driver.save_screenshot(
                    "C:\\Users\\shubham pate\\PycharmProjects\\NonCommerence 16 may "
                    "23\\NonCommerence\\Screenshots\\test_login_002-fail.png")
                assert False

        self.driver.close()
        self.log.info("test_login_002 is Completed")

