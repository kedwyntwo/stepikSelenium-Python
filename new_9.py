from selenium import webdriver
import time
import math
import os
	
try:
	link = "http://suninjuly.github.io/file_input.html"
	driver = webdriver.Firefox()
	driver.get(link)
	input1 = driver.find_element_by_css_selector('input:nth-child(2)')
	input1.send_keys('Ivan')
	input2 = driver.find_element_by_css_selector('input:nth-child(4)')
	input2.send_keys('Petrov')
	input3 = driver.find_element_by_css_selector('input:nth-child(6)')
	input3.send_keys('Smolensk@kek.wait')
	knopka = driver.find_element_by_css_selector('#file')
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'text.txt')
	knopka.send_keys(file_path)
	button = driver.find_element_by_css_selector('body > div > form > button')
	button.click()
	

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

