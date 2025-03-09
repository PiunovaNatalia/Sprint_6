from confest import get_driver
from pages.order_page import OrderPage
import pytest
import allure
from data import Data


class TestOrderPage:
    driver = None

    @classmethod
    @allure.title('Создаем браузер')
    def setup_class(cls):
        cls.driver = get_driver()

    @classmethod
    @allure.title('Закрываем браузер')
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize('order_data', Data.ORDER_TEST_DATA)
    @allure.title('Тестирование создания заказа по кнопке В ШАПКЕ страницы')
    @allure.description(
        'Открываем главную страницу, нажимаем по кнопке «Заказать» в шапке страницы. '
        'Переходим на форму, заполняем первую форму, жмем далее, '
        'заполняем вторую форму, жмем заказать.'
    )
    def test_make_order_with_header_button(self, order_data):
        name, surname, address, station, number, period, day = order_data

        page = OrderPage(self.driver)
        page.open_home_page()

        make_order_header_button = page.get_make_order_header_button()
        make_order_header_button.click()

        page.write_data_in_first_form(page, name, surname, address, station, number)
        page.go_to_next_form()
        page.write_data_in_second_form(page, period, day)

        created_order_text = page.make_order()

        assert "Заказ оформлен" in created_order_text

    @pytest.mark.parametrize('order_data', Data.ORDER_TEST_DATA)
    @allure.title('Тестирование создания заказа по кнопке В КОНЦЕ страницы')
    @allure.description(
        'Открываем главную страницу, делаем скролл вниз, пока не появится кнопка «Заказать».'
        'Нажимаем на нее и переходим на форму, заполняем первую форму, жмем далее, '
        'заполняем вторую форму, жмем заказать.'
    )
    def test_make_order_with_bottom_button(self, order_data):
        name, surname, address, station, number, period, day = order_data

        page = OrderPage(self.driver)
        page.open_home_page()

        # Кнопка внизу страницы
        make_order_footer_button = page.get_make_order_footer_button()
        page.page_scroll_down()
        make_order_footer_button.click()

        page.write_data_in_first_form(page, name, surname, address, station, number)
        page.go_to_next_form()
        page.write_data_in_second_form(page, period, day)

        created_order_text = page.make_order()

        assert "Заказ оформлен" in created_order_text

    @pytest.mark.parametrize('order_data', Data.ORDER_TEST_DATA)
    @allure.title('Тестирование перехода на галавную страницу после создания заказа')
    @allure.description(
        'Проделываем шаги из теста test_make_order_with_header_button, '
        'но на последнем шаге добавляем переход на страницу статуса и '
        'на этой странице жмем по логотипу Самокат'
    )
    def test_open_home_page_after_making_order(self, order_data):
        name, surname, address, station, number, period, day = order_data

        page = OrderPage(self.driver)
        page.open_home_page()
        make_order_header_button = page.get_make_order_header_button()
        make_order_header_button.click()
        page.write_data_in_first_form(page, name, surname, address, station, number)
        page.go_to_next_form()
        page.write_data_in_second_form(page, period, day)
        page.make_order()

        page.open_status_page()
        page.click_scooter_logo()
        page.wait_for_load_home_page()
        url = page.get_current_url()

        assert url == Data.HOME_PAGE_URL
