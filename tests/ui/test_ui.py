import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # create browser control object
    driver = webdriver.Chrome(service=Service(r'chromedriver.exe'))

    # open web page
    driver.get('https://github.com/login')

    # find login field
    login_elem = driver.find_element(By.ID, 'login_field')

    # enter wrong name or email
    login_elem.send_keys('sergiibutenko@mistakeinemail.com')

    # find password field
    pass_elem = driver.find_element(By.ID, 'password')

    # enter wrong password
    pass_elem.send_keys('wrong password')

    # find sign in button
    btn_elem = driver.find_element(By.NAME, 'commit')

    # left button click
    btn_elem.click()

    # check page title
    assert driver.title == 'Sign in to GitHub · GitHub'

    # close the browser
    driver.close()
