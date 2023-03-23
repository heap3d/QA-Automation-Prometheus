from time import sleep
import pytest
from modules.ui.page_objects.rozetka_page import RozetkaPage


@pytest.mark.rozetka
def test_main_page(rozetka: RozetkaPage):
    rozetka.go_main()
    expected = "Інтернет-магазин ROZETKA™: офіційний сайт найпопулярнішого онлайн-гіпермаркету в Україні"
    assert rozetka.check_title(expected)


@pytest.mark.rozetka
def test_computers_notebooks_menu(rozetka: RozetkaPage):
    rozetka.go_computers_notebooks()
    expected = "Комп'ютери та ноутбуки - ROZETKA | Комп'ютери та ноутбуки у Києві, Харкові, Одесі, Львові: ціна, відгуки, продаж оптом комп'ютерів і ноутбуків"
    assert rozetka.check_title(expected)


@pytest.mark.rozetka
def test_tablets_menu(rozetka: RozetkaPage):
    rozetka.go_tablets()
    expected = "Планшети — купити планшет в Києві: ціна, відгуки | ROZETKA"
    assert rozetka.check_title(expected)


@pytest.mark.rozetka
def test_click_filter_rozetka(rozetka: RozetkaPage):
    rozetka.go_tablets()
    assert rozetka.filter_rozetka()


@pytest.mark.rozetka
def test_add_to_compare(rozetka: RozetkaPage):
    rozetka.go_tablets()
    assert rozetka.is_compared(1)


@pytest.mark.rozetka
def test_compare_bin(rozetka: RozetkaPage):
    rozetka.go_tablets()
    assert rozetka.check_header_compare_num(3)


@pytest.mark.rozetka
def test_open_compare(rozetka: RozetkaPage):
    rozetka.go_tablets()
    rozetka.open_compare_page(3)
    expected = "Порівнюємо планшети | Інтернет-магазин ROZETKA"
    assert rozetka.check_title(expected)


@pytest.mark.rozetka
def test_clear_compare_bin(rozetka: RozetkaPage):
    rozetka.go_tablets()
    count = 3
    for i in range(1, count+1):
        rozetka.click_compare(i)
    assert rozetka.clear_compare_bin(3)
