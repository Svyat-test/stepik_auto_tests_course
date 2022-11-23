# Description
# Справка по: чекбоксам, получению данных из атрибута, скролла, выпадающему списку, аттачу, алерты, переключение окна

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
browser = webdriver.Chrome()


# Выбираем чекбокс
option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
option1.click()


# Получаем атрибут с помощью метода get_attribute (можем проверить наличие атрибута на странице)
robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
# Тут нам вернется булево значение, которое напишет отсутствует ли атрибут "checked" или нет
assert robots_checked is None


# Скролл страницы с помощью js попиксельно
browser.execute_script("window.scrollBy(0, 100);")


# Выпадающий список. Несколько вариантов:
# Нашли элемент на странице по тегу
select = Select(browser.find_element(By.TAG_NAME, "select"))
# Выбираем по значению value, клик здесь не нужен. Метод сам кликает
select.select_by_value("1")
# Можно искать по тексту в выпадашке
select.select_by_visible_text("text")
# Можно искать по индексу (порядковому номеру) в выпадашке (номер начинается с 0). Выберет первое значение в списке
select.select_by_index(0)


# Аттач
# Сначала находим файл, который лежит в той же директории, что и проект -> Находим кнопку аттача -> Прикрепляем аттач файл
os.path.abspath(os.path.dirname(__file__))
browser.find_element(By.TAG_NAME, 'attach_button').send_keys(__file__)


# Алерты / конфирмы (алерт с "отмена" и "ок") / prompt (с полем для ввода текста)
# Первой строкой переключаем фокус на окно с алертом
alert = browser.switch_to.alert
# жмем на нем "ок"
alert.accept()
# если у нас алерт-confirm, то его можно отклонить
alert.dismiss()
# Получение текста из алерта
alert = browser.switch_to.alert
alert_text = alert.text
# алерт - промпт
prompt = browser.switch_to.alert
# Отправляем в текстовое поле "My answer"
prompt.send_keys("My answer")
prompt.accept()


# Переключение окна + правильный код. Не забывай закрывать браузер, для этого используй try / finally
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = ('http://suninjuly.github.io/redirect_accept.html')
    browser.get(link)
    # Здесь запоминаем первое окно
    # firs_window = browser.window_handles[0]
    browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary').click()
    # После клика выше нас редиректнуло на новую страницу. Мы ее запомнили в переменную
    new_window = browser.window_handles[1]
    # Это командой мы переключились на ранее запомненную вторую вкладку
    browser.switch_to.window(new_window)
    a = browser.find_element(By.ID, 'input_value').text
    b = calc(a)
    browser.find_element(By.ID,'answer').send_keys(b)
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    alert = browser.switch_to.alert.text
    print(alert)
    # Здесь теоретически мы могли бы переключиться на исходную первую вкладку
    # browser.switch_to.window(firs_window)
    time.sleep(5)
finally:
    browser.quit()


# Ожидание Implicit Waits. Применять, когда кнопка/элемент не видимы на странице. Но нужно подождать какое-то время пока элемент появится
# на странице. Методу задали 5 секунд, значит: он будет ждать каждый элемент в течение 5 сек, но при этом он автоматически ищет элемент с
# периодичностью 500 мс.
browser.implicitly_wait(5)


# Явные ожидания. Explicit Waits (WebDriverWait и expected_conditions). Применять, когда нужно подождать. Например, пока кнопка станет
# кликабельной, пока текст поменяется. Или кнопка может быть перекрыта каким-то другим элементом. Добавляются +2 библиотеки
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()

# Этот метод ждет, пока в элементе появится определенный текст
text_to_be_present_in_element
# Например, ждет 12с. Пока цена не достигнет заданной нами значнеия
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "тут id"), "тут цена"))




