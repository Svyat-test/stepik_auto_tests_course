
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

# Находим и нажимаем кнопку для перехода дальше
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

# Переходим на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

# Находим Х и вычисляем значение
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

#Находим поле ввода ответа и вписываем туда значение Y.

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

# Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()