import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Open browser

class Testseleniumbasic:
    def browsers(self):
        open_browser = webdriver.Chrome()
        open_browser.implicitly_wait(20)
        return open_browser

    def open_url(self):
        app_url = "https://app.vwo.com/#/login"
        return app_url

    def test_login_neagtive(self):
        browser = self.browsers()
        url = self.open_url()
        # Open url
        browser.get(url)
        # Enter Mail
        browser.find_element(By.ID, "login-username").send_keys("testmail@gmail.com")
        # Enter Password
        browser.find_element(By.ID, "login-password").send_keys("Password@123")
        # Click
        browser.find_element(By.ID, "js-login-btn").click()
        # time
        wait = WebDriverWait(browser, 20)
        # Validation
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class ='notification-box-description']"),
                                                    "Your email, password, IP address or location did not match"))

    def test_login_postive(self):
        browser = self.browsers()
        url = self.open_url()
        # Open url
        browser.get(url)
        # Enter Mail
        browser.find_element(By.ID, "login-username").send_keys("contact+atb5x@thetestingacademy.com")
        # Enter Password
        browser.find_element(By.ID, "login-password").send_keys("ATBx@1234")
        # Click
        browser.find_element(By.ID, "js-login-btn").click()
        # time
        wait = WebDriverWait(browser, 20)
        # Validation
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='Fw(semi-bold) ng-binding']"),
                                                    "Aman"))



