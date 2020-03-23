from selenium import webdriver
import time

try:
    # Ссылка на сайт без ошибки
    link = "http://suninjuly.github.io/registration1.html"

    # Ссылка на сайт с ошибкой
    # link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    name = browser.find_element_by_css_selector(".first_block .first")
    name.send_keys("Ivan")
    surname = browser.find_element_by_css_selector(".first_block .second")
    surname.send_keys("Petrov")
    mail = browser.find_element_by_css_selector(".first_block .third")
    mail.send_keys("ip@mail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()