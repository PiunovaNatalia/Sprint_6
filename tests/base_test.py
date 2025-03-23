import allure
from confest import get_driver


class BaseTest:
    """
    Вместо фикстур разместила открытие и закрытие браузера
    в базовом класссе для тестов.

    1. В задании была рекомендация использовать setup_class и teardown_class
    2. Таким образом можно избавиться от дублирования
    """
    driver = None

    @classmethod
    @allure.title('Создаем браузер')
    def setup_class(cls):
        cls.driver = get_driver()

    @classmethod
    @allure.title('Закрываем браузер')
    def teardown_class(cls):
        cls.driver.quit()