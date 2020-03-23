from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
try:
	browser = webdriver.Firefox()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	price = WebDriverWait (browser, 15).until(
	EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price',), '$100')
	)
	button1 = browser.find_element_by_css_selector('#book')	
	button1.click()
	value = browser.find_element_by_css_selector('#input_value')
	chislo = value.text
	x = int(chislo)
	y = calc(x)
	input1 = browser.find_element_by_css_selector('#answer')
	input1.send_keys(y)
	button2 = browser.find_element_by_css_selector('#solve')
	button2.click()

finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()