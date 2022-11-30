from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


# Находим радиобаттон со значением по умолчанию - checked.

    people_radio = browser.find_element(By.ID, "robotsRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
# Т.к. у данного атрибута checked значение не указано явно (не checked равно чему-то), то метод get_attribute вернёт "true".


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()