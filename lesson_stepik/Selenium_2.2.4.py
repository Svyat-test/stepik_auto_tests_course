# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"


from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

#Заполняем поля ввода данных
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("bla")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("blabla")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("blablabla")

#Создаем файл для загрузки

    with open('test.txt', 'w') as file1:
        file1.write('blablabla test')

#Формируем путь до файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

#Находим элемент загрузки файла и загружаем его

    element_file = browser.find_element(By.ID, "file")
    element_file.send_keys(file_path)

# Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

