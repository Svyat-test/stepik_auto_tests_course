import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Проверка двух тестовых страниц от степика.

class TestPage(unittest.TestCase):
    def test_Page2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your name']").send_keys("Name")
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your mail']").send_keys("email")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(3)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text, 'Приветственное сообщение неправильное или не найден элемент'
        browser.quit()

    def test_Page1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']").send_keys("first ame")
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']").send_keys("Last name")
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']").send_keys("email")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(3)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text, 'Приветственное сообщение неправильное или не найден элемент'
        browser.quit()

if __name__ == "__main__":
    unittest.main()
