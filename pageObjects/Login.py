import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    Text_Email_XPATH = (By.XPATH, "//input[@id='Email']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='Password']")
    Click_Login_XPATH = (By.XPATH, "//button[@type='submit']")
    CLick_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Enter_Email(self, email):
        self.driver.find_element(*LoginPage.Text_Email_XPATH).clear()
        self.driver.find_element(*LoginPage.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*LoginPage.Text_Password_XPATH).clear()
        self.driver.find_element(*LoginPage.Text_Password_XPATH).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*LoginPage.Click_Login_XPATH).click()

    def Click_Logout(self):
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//i[@class='fas fa-cogs']")))
        self.driver.find_element(*LoginPage.CLick_Logout_XPATH).click()


