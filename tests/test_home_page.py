from confest import get_driver
from pages.home_page import HomePage
from data import Data
import pytest
import allure


class TestHomePage:
    driver = None

    @classmethod
    @allure.title('Создаем браузер')
    def setup_class(cls):
        cls.driver = get_driver()

    @classmethod
    @allure.title('Закрываем браузер')
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('Тестирование раздела «Вопросы о важном»: вопрос №{item_number}')
    @allure.description(
        'Открываем главную страницу, делаем скролл вниз, пока не появится раздел «Вопросы о важном».'
        'Нажимаем на каждый из вопросов, ждем появления текста ответа.'
    )
    @pytest.mark.parametrize('item_number', HomePage.accordion_items_ids)
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
        page.open_home_page()
        page.page_scroll_down()

        according_button = page.get_according_button(item_number)
        page.click_accordion_button(according_button, item_number)

        according_panel = page.get_according_panel(item_number)

        assert according_panel.is_displayed and according_panel.text == page.accordion_items_text[item_number]

    @allure.title('Тестирование открытия страницы Яндекса')
    @allure.description(
        'Открываем главную страницу, нажимаем на логотип Яндекс в шапке сайт. '
        'Переходим на сайта Яндекс.'
    )
    def test_open_yandex_page(self):
        page = HomePage(self.driver)
        page.open_home_page()
        page.click_yandex_logo()
        page.switch_to_yandex_tab()
        url = page.get_current_url()

        assert Data.YANDEX_URL in url