
# Ваша программа должна выполнить следующие шаги:
#
# Открыть страницу https://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
# Находим значение Х и вычисляем значение Y через функцию, описанную выше.

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
#Находим поле ввода ответа и вписываем туда значение Y.

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
#Находим чекбокс с надписью Робот и ставим галочку.

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

# Находим радиобаттон с надписью Роботы рулят и ставим галочку.

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
# Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()