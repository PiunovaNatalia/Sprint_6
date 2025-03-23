from pages.home_page import HomePage
from data import Data
import pytest
import allure
from base_test import BaseTest


class TestHomePage(BaseTest):
    @allure.title('Тестирование раздела «Вопросы о важном»: вопрос №{item_number}')
    @allure.description(
        'Открываем главную страницу, делаем скролл вниз, пока не появится раздел «Вопросы о важном».'
        'Нажимаем на каждый из вопросов, ждем появления текста ответа.'
    )
    @pytest.mark.parametrize('item_number', Data.ACCORDION_ITEMS_IDS)
    def test_accordion(self, item_number):
        """
        Тест с параметризацией на все элементы из
        выпадающего списка в разделе «Вопросы о важном».

        Несмотря на то, что в задани написано:
            'Важно написать отдельный тест на каждый вопрос.'

        Я посчитала, что это не оптимально и это хороший тест-кейс,
        где можно применить параметризацию, ведь в задании сказано:
            'Обязательно используй параметризацию. Где именно — подумай самостоятельно'.
        """

        page = HomePage(self.driver)
        page.open_page(Data.HOME_PAGE_URL)
        page.wait_for_visibility_of_element(page.home_header__header)

        page.page_scroll_down()
        page.wait_for_visibility_of_element(page.home_faq)
        according_button = page.get_according_button(item_number)
        page.click_accordion_button(according_button, item_number)
        according_panel = page.get_according_panel(item_number)

        assert according_panel.is_displayed() and according_panel.text == Data.ACCORDION_ITEMS_TEXT[item_number]

    @allure.title('Тестирование открытия страницы Яндекса')
    @allure.description(
        'Открываем главную страницу, нажимаем на логотип Яндекс в шапке сайт. '
        'Переходим на сайта Яндекс.'
    )
    def test_open_yandex_page(self):
        page = HomePage(self.driver)
        page.open_page(Data.HOME_PAGE_URL)
        page.wait_for_visibility_of_element(page.home_header__header)

        page.click_yandex_logo()
        page.switch_to_next_window()
        page.wait_for_number_of_windows_to_be_two()
        open_window_num = page.get_number_of_open_windows()

        assert open_window_num == Data.NEEDED_OPEN_WINDOW_NUMBER
