from selenium import webdriver
import time
import math
import os
	
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	driver = webdriver.Firefox()
	driver.get(link)
	gotobutton = driver.find_element_by_css_selector('.btn-primary')
	gotobutton.click()
	new_window = driver.window_handles[1]
	driver.switch_to.window(new_window)
	time.sleep(1)
	treasure = driver.find_element_by_css_selector('#input_value')
	chislo = treasure.text
	x = int(chislo)
	y = calc(x)
	otvet = driver.find_element_by_css_selector('#answer')
	otvet.send_keys(y)
	button = driver.find_element_by_css_selector('body > form > div > div > button')
	button.click()
	
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()