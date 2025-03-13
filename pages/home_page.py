from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage


class HomePage(BasePage):
    home_faq = (By.XPATH, ".//div[contains(@class,'Home_FAQ')]")
    logo_yandex__header_link = (By.XPATH, "(.//a[contains(@class,'Header_LogoYandex')])")
    yandex_page_block = (By.XPATH, "(.//div[contains(@class,'search3__logo')])")
    accordion_item_button__locator_template = ".//div[@id='accordion__heading-{item_number}']"
    accordion_item_panel__locator_template = ".//div[@id='accordion__panel-{item_number}']"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    @allure.step('Переключаемся на новое окно')
    def switch_to_next_window(self):
        self.switch_to_window_by_num(1)

    @allure.step('Ищем вопрос №{item_number}')
    def get_according_button(self, item_number):
        xpath = (
            By.XPATH,
            self.accordion_item_button__locator_template.format(item_number=item_number-1)
        )
        return self.get_element(xpath)

    @allure.step('Ищем блок с ответом на вопрос №{item_number}')
    def get_according_panel(self, item_number):
        xpath = (
            By.XPATH,
            self.accordion_item_panel__locator_template.format(item_number=item_number - 1)
        )
        self.wait_for_visibility_of_element(xpath)
        accordion_panel = self.get_element(xpath)
        return accordion_panel

    @allure.step('Нажимаем на элемент с вопросом №{item_number}')
    def click_accordion_button(self, accordion_button, item_number):
        self.execute_click_script(accordion_button)

    @allure.step('Нажимаем на логотип Яндекс')
    def click_yandex_logo(self):
        self.click(self.logo_yandex__header_link)
