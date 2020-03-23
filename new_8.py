from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


try:
	link = "http://suninjuly.github.io/selects1.html"
	driver=webdriver.Firefox()
	driver.get(link)
	first_num = driver.find_element_by_css_selector('#num1')
	fnum=first_num.text
	x=int(fnum)
	second_num = driver.find_element_by_css_selector('#num2')
	secnum=second_num.text
	y=int(secnum)
	summ = x+y
	summ1=str(summ)
	select = Select(driver.find_element_by_css_selector('.custom-select'))
	select.select_by_value(summ1)

	button = driver.find_element_by_css_selector("button.btn")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()