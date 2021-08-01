from selenium import webdriver
import time
#ожидание кнопки
try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
    # На каждый вызов команды find_element WebDriver будет ждать 5 сек до появления элемента на странице
    # прежде, чем
    # выбросить
    # исключение
    # NoSuchElementException.
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()