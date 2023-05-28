import time

import pytest


from pageObjects.Login import LoginPage
from utilites import XLutilities
from utilites.ReadProperties import ReadConfig
from utilites.logger import LogGenerator

class Test_Login_DDT:
    Url = ReadConfig.URL()
    # username = Readconfig.getusername()
    # password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "C:\\Users\\shubham pate\\PycharmProjects\\NonCommerence 16 may " \
           "23\\NonCommerence\\testCases\\TestData\\login.xlsx "

    def test_login_ddt(self, setup):
        self.driver = setup
        self.log.info("test_login_ddt is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)
        self.lp = LoginPage(self.driver)
        time.sleep(10)
        self.rows = XLutilities.getrowCount(self.path, 'Sheet1')
        print("Number of rows are --->", self.rows)
        login_stuats = []
        for r in range(2, self.rows + 1):
            self.email = XLutilities.readData(self.path, 'Sheet1', r, 2)
            self.password = XLutilities.readData(self.path, 'Sheet1', r, 3)

            self.lp.Enter_Email(self.email)
            self.log.info("Entering username-->" + self.email)
            self.lp.Enter_Password(self.password)
            self.log.info("Entering password-->" + self.password)
            self.lp.Click_Login()
            self.log.info("Click on login button")

            if self.driver.title == "Dashboard / nopCommerce administration":

                self.driver.save_screenshot(
                    "C:\\Users\\shubham pate\\PycharmProjects\\NonCommerence 16 may 23\\NonCommerence\\Screenshots\\" + self.email + self.password + "test_login_ddt-pass.png")

                self.lp.Click_Logout()
                self.log.info("Click on logout button")

                login_stuats.append("Pass")
                XLutilities.writeData(self.path, 'Sheet1', r, 4, "Pass")
            else:

                login_stuats.append("Fail")
                XLutilities.writeData(self.path, 'Sheet1', r, 4, "Fail")
                self.driver.save_screenshot(
                    "C:\\Users\\shubham pate\\PycharmProjects\\NonCommerence 16 may 23\\NonCommerence\\Screenshots\\" + self.email + self.password + "test_login_ddt-fail.png")
                # assert False

        print(login_stuats)
        if "Fail" not in login_stuats:
            self.log.info("test_login_ddt is Passed")
            assert True
        else:
            self.log.info("test_login_ddt is Failed")
            assert False
        self.driver.close()
        self.log.info("test_login_ddt is Completed")