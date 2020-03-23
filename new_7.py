from selenium import webdriver
import time
import math
def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/get_attribute.html"
	driver=webdriver.Firefox()
	driver.get(link)
	treasure = driver.find_element_by_xpath('//img')
	x = treasure.get_attribute('valuex')
	y = calc(x)
	input1 = driver.find_element_by_css_selector('#answer')
	input1.send_keys(y)
	option1=driver.find_element_by_css_selector('#robotcheckbox')
	option1.click()
	option2=driver.find_element_by_css_selector('#robotsrule')
	option2.click() 

	button = driver.find_element_by_css_selector("button.btn")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()