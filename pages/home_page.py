from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from .base_page import BasePage


class HomePage(BasePage):
    home_header__header = (By.XPATH, ".//div[contains(@class,'Home_Header')]")
    home_faq = (By.XPATH, ".//div[contains(@class,'Home_FAQ')]")

    logo_yandex__header_link = (By.XPATH, "(.//a[contains(@class,'Header_LogoYandex')])")
    yandex_page_block = (By.XPATH, "(.//div[contains(@class,'search3__logo')])")

    accordion_item_button__locator_template = ".//div[@id='accordion__heading-{item_number}']"
    accordion_item_panel__locator_template = ".//div[@id='accordion__panel-{item_number}']"

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    @allure.step('Переключаемся на новое окно')
    def switch_to_next_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получаем количество открытых окон')
    def get_number_of_open_windows(self):
        return len(self.driver.window_handles)

    @allure.step('Ищем вопрос №{item_number}')
    def get_according_button(self, item_number):
        xpath = self.accordion_item_button__locator_template.format(item_number=item_number-1)
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step('Ищем блок с ответом на вопрос №{item_number}')
    def get_according_panel(self, item_number):
        xpath = self.accordion_item_panel__locator_template.format(item_number=item_number-1)
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        accordion_panel = self.driver.find_element(By.XPATH, xpath)
        return accordion_panel

    @allure.step('Нажимаем на элемент с вопросом №{item_number}')
    def click_accordion_button(self, accordion_button, item_number):
        self.driver.execute_script("arguments[0].click();", accordion_button)

    @allure.step('Нажимаем на логотип Яндекс')
    def click_yandex_logo(self):
        self.driver.find_element(*self.logo_yandex__header_link).click()
