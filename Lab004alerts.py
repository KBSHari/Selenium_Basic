import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Testalr:

    def test_alerts(self):
        browser=webdriver.Chrome()
        browser.get("https://the-internet.herokuapp.com/javascript_alerts")
        
        #only accpet alert
        browser.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
        #wait until alert present
        wait=WebDriverWait(browser,10)
        wait.until(EC.alert_is_present())
        #switch the driver to alerts
        alerts=browser.switch_to.alert
        #accept the alert
        alerts.accept()
        result_message=browser.find_element(By.XPATH,"//p[@id='result']").text
        print(result_message)

        #alerts having cancel & ok button

        browser.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
        # wait until alert present
        wait = WebDriverWait(browser, 10)
        wait.until(EC.alert_is_present())
        # switch the driver to alerts
        alerts = browser.switch_to.alert
        #cancel the alert
        alerts.dismiss()
        result_message = browser.find_element(By.XPATH, "//p[@id='result']").text
        print(result_message)

        browser.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
        # wait until alert present
        wait = WebDriverWait(browser, 10)
        wait.until(EC.alert_is_present())
        # switch the driver to alerts
        alerts = browser.switch_to.alert
        #accpet the alerts
        alerts.accept()
        result_message = browser.find_element(By.XPATH, "//p[@id='result']").text
        print(result_message)

        # alerts having text box + cancel & ok button

        browser.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
        # wait until alert present
        wait = WebDriverWait(browser, 10)
        wait.until(EC.alert_is_present())
        # switch the driver to alerts
        alerts = browser.switch_to.alert
        # cancel the alert
        alerts.dismiss()
        result_message = browser.find_element(By.XPATH, "//p[@id='result']").text
        print(result_message)

        browser.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
        # wait until alert present
        wait = WebDriverWait(browser, 10)
        wait.until(EC.alert_is_present())
        # switch the driver to alerts
        alerts = browser.switch_to.alert
        #enter text
        alerts.send_keys("Happy")
        # accpet the alerts
        alerts.accept()
        result_message = browser.find_element(By.XPATH, "//p[@id='result']").text
        print(result_message)






