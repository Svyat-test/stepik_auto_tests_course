# Открыть страницу https://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
  return str(int(x) + int(y))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
# Находим сумму двух чисел.

    x_element = browser.find_element(By.ID, "num1")
    x1 = x_element.text
    x_element = browser.find_element(By.ID, "num2")
    x2 = x_element.text
    y = calc(x1, x2)
#Выбираем в выпадающем списке значение равное Y.

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(y)

# Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()