
# pytest -v --driver Chrome --driver-path C:\\chromedrivers\\chromedriver.exe\\chromedriver tests/test_selenium_simple.py

from selenium import webdriver

import time
from selenium.webdriver.common.by import By
import pytest

def test_search_example():
    """ Search some phrase in google and make a screenshot of the page. """
    selenium = webdriver.Chrome('C:/chromedrivers/chromedriver.exe')
    # Open google search page:
    selenium.get('https://google.com')

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    search_input = selenium.find_element(by=By.NAME, value='q')


    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    search_button = selenium.find_element(by=By.NAME, value='btnK')
    search_button.submit()
    # search_button.click()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    selenium.save_screenshot('result.png')
    selenium.close()
    selenium.quit()
