import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


# Open browser

class Testseleniumbasic:
    def browsers(self):
        open_browser = webdriver.Chrome()
        return open_browser

    def open_url(self):
        app_url="https://app.vwo.com/#/login"
        return app_url


    def test_login_neagtive(self):
        browser=self.browsers()
        url=self.open_url()

        # Open url
        browser.get(url)

        # Enter Mail
        browser.find_element(By.ID, "login-username").send_keys("testmail@gmail.com")

        # Enter Password
        browser.find_element(By.ID, "login-password").send_keys("Password@123")

        # Click
        browser.find_element(By.ID, "js-login-btn").click()

        # time
        time.sleep(5)

        # Validation
        error_message = browser.find_element(By.ID, "js-notification-box-msg").text
        assert "Your email, password, IP address or location did not match" == error_message

    def test_login_postive(self,browser):

        browser = self.browsers()
        url = self.open_url()

        # Enter Mail
        browser.find_element(By.ID, "login-username").send_keys("contact+atb5x@thetestingacademy.com")

        # Enter Password
        browser.find_element(By.ID, "login-password").send_keys("ATBx@1234")

        # Click
        browser.find_element(By.ID, "js-login-btn").click()

        # time
        time.sleep(10)

        # Validation
        username = browser.find_element(By.XPATH, '//span[@class="Fw(semi-bold) ng-binding"]').text
        assert "Aman" == username
