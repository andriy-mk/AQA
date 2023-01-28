import pytest


class User:
    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Andrii"
        self.second_name = "Yevushko"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()
