from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
import allure
from time import sleep


class HomePage:
    home_header__header = (By.XPATH, ".//div[contains(@class,'Home_Header')]")
    home_faq = (By.XPATH, ".//div[contains(@class,'Home_FAQ')]")

    logo_yandex__header_link = (By.XPATH, "(.//a[contains(@class,'Header_LogoYandex')])")
    yandex_page_block = (By.XPATH, "(.//div[contains(@class,'search3__logo')])")

    accordion_item_button__locator_template = ".//div[@id='accordion__heading-{item_number}']"
    accordion_item_panel__locator_template = ".//div[@id='accordion__panel-{item_number}']"

    accordion_items_ids = [1, 2, 2, 3, 4, 5, 6, 7, 8]
    accordion_items_text = {
        1: "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        2: "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        3: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        4: "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        5: "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        6: "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        7: "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        8: "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
    }

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем главную страницу')
    def open_home_page(self):
        self.driver.get(Data.HOME_PAGE_URL)
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.home_header__header)
        )

    def wait_for_visibility_of_element_located(self, rule):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(rule)
        )

    @allure.step('Переключаемся на новое окно')
    def switch_to_yandex_tab(self):
        """
        Здесь, к сожалению, пришлось использовать sleep вместо expected_conditions,
        так как ни один из EC не сработал.
        Пыталась зацепиться за yandex_page_block через wait_for_visibility_of_element_located.
        И пробовала EC.new_window_is_opened
        Но самая большая проблема, что после клика по логотипу открывается
        окно "Подтвердите, что запросы отправляли вы, а не робот"
        """

        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(5)

    def get_current_url(self):
        return self.driver.current_url

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

    @allure.step('Прокручиваем страницу вниз')
    def page_scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.wait_for_visibility_of_element_located(self.home_faq)

    @allure.step('Нажимаем на логотип Яндекс')
    def click_yandex_logo(self):
        self.driver.find_element(*self.logo_yandex__header_link).click()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        assert len(self.driver.window_handles) == 2
