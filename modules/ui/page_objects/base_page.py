from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # import module Service


class BasePage:  # описуємо властивості класу
    PATH = r"/Users/andriy/AQA"
    DRIVER_NAME = "chromedriver.exe"

    def __init__(
        self,
    ):  # в конструкторі оголошуємо властивість обєкта та ініціалізуємо її
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()
