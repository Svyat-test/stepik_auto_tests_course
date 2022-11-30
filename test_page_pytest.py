from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    browser = webdriver.Chrome()
    link = 'https://test.pas.vseinstrumenti.net/site/login'
    email = 'autotest@login.ru'
    password = 'Autotest123'
    try:
        browser.get(link)
        browser.find_element(By.ID, 'loginform-username').send_keys(email)
        browser.find_element(By.ID, 'loginform-password').send_keys(password)
        browser.find_element(By.CSS_SELECTOR, '.btn.primary-button').click()
        expected_result = '© Личный кабинет поставщика 2022'
        browser.implicitly_wait(10)
        actual_result = browser.find_element(By.CSS_SELECTOR, '.copyright').text
        assert expected_result == actual_result, f"ожидали: {expected_result}, фактический: {actual_result}"
    finally:
        browser.quit()