from selenium import webdriver
import time

try:
    driver = webdriver.Firefox()
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("123")

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла