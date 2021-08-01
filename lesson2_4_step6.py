from selenium import webdriver
import time
#ожидание кнопки
try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/cats.html")

    button = browser.find_element_by_id("button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    