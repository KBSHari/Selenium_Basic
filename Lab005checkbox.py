import time

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class Testcheckbox:

    def test_checkbox(self):
        browser = webdriver.Chrome()
        browser.get("https://the-internet.herokuapp.com/checkboxes")

        checkboxes = browser.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

        # checkbox selected
        for i in checkboxes:
            if not i.is_selected():
                i.click()

        #checkbox unselected
        for i in checkboxes:
            if i.is_selected():
                i.click()

        time.sleep(5)
