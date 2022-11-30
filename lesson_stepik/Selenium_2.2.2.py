from selenium import webdriver
browser = webdriver.Chrome()
import time
#Использование JS. Изменили заголовок страницы и вызвали алерт:

browser.execute_script("document.title='Script executing';alert('Robots at work');")
time.sleep(10)
browser.quit()