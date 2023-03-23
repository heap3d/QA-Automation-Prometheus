import pytest
from modules.api.clients.github import GitHub
from modules.ui.page_objects.rozetka_page import RozetkaPage


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Dmytro'
        self.second_name = 'Holub'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def rozetka():
    rozetka = RozetkaPage()

    yield rozetka

    rozetka.close()
