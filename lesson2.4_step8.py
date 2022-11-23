import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)
    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element(By.ID, 'book').click()
    browser.execute_script("window.scrollBy(0, 100);")
    a = browser.find_element(By.ID, 'input_value').text
    b = calc(a)
    browser.find_element(By.ID, 'answer').send_keys(b)
    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(5)
    browser.quit()




