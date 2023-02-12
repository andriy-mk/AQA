from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):  # SignInPage унаслідує BasePage
    URL = "https://github.com/login"  # оголошуємо атрибут класу

    def __init__(self):  # конструктор класу
        super().__init__()  # виклик конструктора базового класу

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):  # метод обєкта
        # знаходимо поле, в яке будемо вводити неправильне імя еористувача або поштову адресу
        login_elem = self.driver.find_element(By.ID, "login_field")

        # вводимо неправильне імя користувача або поштову адресу
        login_elem.send_keys(username)

        # знаходимо поле, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        # вводимо неправильний пароль
        pass_elem.send_keys(password)

        # знаходимо кнопку sign im
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
