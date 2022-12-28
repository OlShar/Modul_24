# pytest -v --driver Chrome --driver-path C:\\chromedrivers\\chromedriver.exe\\chromedriver test_selenium_petfriends.py
import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


# @pytest.mark.usefixtures('chrome_options')
def test_petfriends():
    # Open PetFriends base page:
    selenium= webdriver.Chrome('C:/chromedrivers/chromedriver.exe')
    selenium.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = selenium.find_element(by=By.XPATH, value="//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    # click existing user button
    btn_exist_acc = selenium.find_element(by=By.LINK_TEXT, value="У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = selenium.find_element(by=By.ID, value="email")
    field_email.click()
    field_email.clear()
    field_email.send_keys("testsapi@gmail.com")

    # add password
    field_pass = selenium.find_element(by=By.ID, value="pass")
    field_pass.click()
    field_pass.clear()
    field_pass.send_keys("asdf5577")

    # click submit button
    btn_submit = selenium.find_element(by=By.XPATH, value="//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!
    if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")