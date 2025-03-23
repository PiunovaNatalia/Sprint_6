from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    home_header__header = (By.XPATH, ".//div[contains(@class,'Home_Header')]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу {url}')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Ожидаем отображения элемента на странице')
    def wait_for_visibility_of_element(self, xpath):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(xpath))

    @allure.step('Ожидаем скрытия элемента на странице')
    def wait_for_invisibility_of_element(self, xpath):
        WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located(xpath))

    @allure.step('Получаем URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Прокручиваем страницу вниз')
    def page_scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Ожидаем открытия окна')
    def wait_for_number_of_windows_to_be_two(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

    @allure.step('Ищем элемент на странице')
    def get_element(self, xpath):
        return self.driver.find_element(*xpath)

    @allure.step('Кликаем по кнопке')
    def click(self, xpath):
        self.get_element(xpath).click()

    @allure.step('Переключаемся на окно №{window_number}')
    def switch_to_window_by_num(self, window_number):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step('Получаем количество открытых окон')
    def get_number_of_open_windows(self):
        return len(self.driver.window_handles)

    @allure.step('Выполняем скрипт по нажатию кнопки')
    def execute_click_script(self, element):
        self.driver.execute_script("arguments[0].click();", element)
