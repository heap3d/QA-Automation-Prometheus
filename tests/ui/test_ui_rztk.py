from multiprocessing.connection import wait
from time import sleep
import pytest
from modules.ui.page_objects.rztk_page import RZTKPage


@pytest.mark.rztk
def test_user_button():
    first_page = RZTKPage()

    first_page.go_to()
    first_page.try_login('user', 'pass')
    sleep(5)
