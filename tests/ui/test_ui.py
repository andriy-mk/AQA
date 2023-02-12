import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # import module Service
from selenium.webdriver.common.by import By
# import time


@pytest.mark.ui
def test_check_incorrect_username():
    # створення обєкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r"/Users/andriy/AQA" + "chromedriver.exe")
    )

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # знаходимо поле, в яке будемо вводити неправильне імя еористувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # вводимо неправильне імя користувача або поштову адресу
    login_elem.send_keys("test@gmail.com")

    # знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    # знаходимо кнопку sign im
    btn_elem = driver.find_element(By.NAME, "commit")

    # емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"
    # time.sleep(3)

    # закриваємо браузер
    driver.close
