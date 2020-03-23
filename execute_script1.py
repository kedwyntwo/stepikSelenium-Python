from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
		
try:
	link = "http://SunInJuly.github.io/execute_script.html"
	driver = webdriver.Firefox()
	driver.get(link)
	button = driver.find_element_by_tag_name('button')
	driver.execute_script("return arguments[0].scrollIntoView(true);", button)
	treasure = driver.find_element_by_css_selector('#input_value')
	chislo = treasure.text
	x = int(chislo)
	y = calc(x)
	input1 = driver.find_element_by_css_selector('#answer')
	input1.send_keys(y)
	option1 = driver.find_element_by_css_selector('#robotcheckbox')
	option1.click()
	option2 = driver.find_element_by_css_selector('#robotsrule')
	option2.click() 
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

