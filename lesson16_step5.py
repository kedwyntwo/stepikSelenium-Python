from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    driver = webdriver.Firefox()
    driver.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = driver.find_element_by_xpath("//div/div[1]/input[@required]")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_xpath("//div/div[2]/input[@required]")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_xpath("//div/div[3]/input[@required]")
    input3.send_keys("Smolensk")
    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_css_selector("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(200)
    # закрываем браузер после всех манипуляций
    driver.quit()