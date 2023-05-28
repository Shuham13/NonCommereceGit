import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login import LoginPage
from utilites.ReadProperties import ReadConfig
from utilites.logger import LogGenerator
from selenium.webdriver.support import expected_conditions as EC


class Test_Login:
    url = ReadConfig.URL()
    email = ReadConfig.Email()
    password = ReadConfig.Password()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.log.info("Test login Started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.lp = LoginPage(self.driver)
        self.driver.get(self.url)
        self.log.info("Going to Url -->" + self.url)
        self.lp.Enter_Email(self.email)
        self.log.info("Entering Email-->" + str(self.email))
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.Click_Login()
        self.log.info("Clicking Login")
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.driver.save_screenshot(
                "C:\\Users\\shubham pate\\PycharmProjects\\NonCommerence 16 may 23\\NonCommerence\\Screenshots"
                "\\test_page_title_pass.PNG")
            self.lp.Click_Logout()
            assert True
            self.log.info("test_login is Passed")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\shubham pate\\PycharmProjects\\NonCommerence 16 may 23\\NonCommerence\\Screenshots"
                "\\test_page_title_fail.PNG")
            assert False
            self.log.info("test_login is Failed")
        self.log.info("test_login is Completed")
