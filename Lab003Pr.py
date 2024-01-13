import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAssig:

    def test_ebay(self):
       browser= webdriver.Chrome()
       browser.get("https://www.ebay.com/b/PC-Laptops-Netbooks/177/bn_317584")
       search_box=browser.find_element(By.XPATH,"//input[@id='gh-ac']")
       search_box.send_keys("16GB")
       search_btn = browser.find_element(By.XPATH, "//input[@id='gh-btn']")
       search_btn.click()
       headings=browser.find_elements(By.XPATH,"//span[@role='heading']")
       price=browser.find_elements(By.XPATH,"//span[@class='s-item__price']")

       for i in range(0,len(headings)):
          print(headings[i].text)
          print(price[i].text)

















