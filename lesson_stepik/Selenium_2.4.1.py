# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Находим кнопку для бронирования
    button1 = browser.find_element(By.ID, 'book')

# Ожидаем появления в поле прайс значения $100
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

# Нажимаем кнопку для бронирования
    button1.click()

# Находим значение Х и отправляем в функцию для вычисления
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

# Находим поле для ответа и вносим туда вычисленное значение
    answer_line = browser.find_element(By.ID, 'answer')
    answer_line.send_keys(y)

# Находим кнопку для ответа и нажимаем ее
    button2 = browser.find_element(By.ID, 'solve')
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
