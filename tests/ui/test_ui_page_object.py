from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():  # даємо назву тесту
    # створення обєкту сторінки
    sign_in_page = SignInPage()  # створюємо обєкт сторінки для взаємодії з нею

    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_obj@gmail.com", "wrong_password")

    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # закриваємо браузер
    sign_in_page.close()
