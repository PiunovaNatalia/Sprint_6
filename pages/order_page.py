from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from data import Data


class OrderPage:
    make_order__header_button = (By.XPATH, "(.//div[contains(@class,'Header_Nav')]/button[text()='Заказать'])")
    order_status__header_button = (By.XPATH, "(.//div[contains(@class,'Header_Nav')]/button[text()='Статус заказа'])")
    make_order__footer_button = (By.XPATH, "(.//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать'])")
    scooter__header_link = (By.XPATH, ".//a[contains(@class,'Header_LogoScooter')]")
    order_page_header = (By.XPATH, "(.//div[contains(@class,'Order_Header')])")
    home_header__header = (By.XPATH, "(.//div[contains(@class,'Home_Header')])")

    name_input = (By.XPATH, "(.//     input[contains(@class,'Input_Input')])[2]")
    surname_input = (By.XPATH, "(.//input[contains(@class,'Input_Input')])[3]")
    address_input = (By.XPATH, "(.//input[contains(@class,'Input_Input')])[4]")
    metro_station_input = (By.XPATH, "(.//input[@class='select-search__input'])")
    number_input = (By.XPATH, "(.//input[contains(@class,'Input_Input')])[5]")

    selected_station_template = ".//div[(contains(@class,'Order_Text')) and (text()='{metro_station}')]"
    select_input = (By.XPATH, ".//div[contains(@class,'select-search__select')]")
    button_next = (By.XPATH, ".//button[(contains(@class,'Button_Button')) and (text()='Далее')]")
    look_order_status = (By.XPATH, ".//button[(contains(@class,'Button_Button')) and (text()='Посмотреть статус')]")

    header_about_rent = (By.XPATH, ".//div[(contains(@class,'Order_Header')) and (text()='Про аренду')]")
    rent_time_button = (By.XPATH, ".//div[contains(@class,'Dropdown-placeholder')]")
    drop_down_menu = (By.XPATH, ".//div[contains(@class,'Dropdown-menu')]")
    drop_down_menu_option_template = ".//div[(contains(@class,'Dropdown-option')) and (text()='{period}')]"

    datepicker_input = (By.XPATH, ".//div[contains(@class,'react-datepicker__input-container')]/input")
    opened_datepicker = (By.XPATH, ".//div[contains(@class,'react-datepicker__month-container')]")

    datepicker_pick_day_template = ".//div[(contains(@class,'react-datepicker__day')) and (text()='{day}')]"

    final_order_button = (By.XPATH, ".//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']")

    order_modal = (By.XPATH, ".//div[contains(@class,'Order_Modal')]")
    button_yes = (By.XPATH, ".//button[(contains(@class,'Button_Button')) and (text()='Да')]")
    order_modal__header = (By.XPATH, ".//div[contains(@class,'Order_ModalHeader')]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем главную страницу')
    def open_home_page(self):
        self.driver.get(Data.HOME_PAGE_URL)
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.home_header__header)
        )

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.home_header__header)
        )

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.order_page_header)
        )

    def wait_for_visibility_of_element_located(self, rule):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(rule)
        )

    def wait_for_invisibility_of_element_located(self, rule):
        WebDriverWait(self.driver, 3).until(
            EC.invisibility_of_element_located(rule)
        )

    def get_make_order_header_button(self):
        return self.driver.find_element(*self.make_order__header_button)

    def get_make_order_footer_button(self):
        return self.driver.find_element(*self.make_order__footer_button)

    @allure.step('Вводим имя')
    def set_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    @allure.step('Вводим фамилию')
    def set_surname(self, surname):
        self.driver.find_element(*self.surname_input).send_keys(surname)

    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    @allure.step('Выбираем станцию метро')
    def set_metro_station(self, metro_station):
        self.driver.find_element(*self.metro_station_input).click()
        self.wait_for_visibility_of_element_located(self.select_input)

        selected_station = (
            By.XPATH,
            self.selected_station_template.format(metro_station=metro_station)
        )
        self.driver.find_element(*selected_station).click()

        self.wait_for_invisibility_of_element_located(self.select_input)

    @allure.step('Вводим номер телефона')
    def set_number(self, number):
        self.driver.find_element(*self.number_input).send_keys(number)

    @allure.step('Нажимаем кнопку Далее')
    def go_to_next_form(self):
        self.driver.find_element(*self.button_next).click()
        self.wait_for_visibility_of_element_located(self.header_about_rent)

    @allure.step('Выбираем период аренды самоката')
    def set_rent_period(self, period):
        self.driver.find_element(*self.rent_time_button).click()
        self.wait_for_visibility_of_element_located(self.drop_down_menu)
        selected_period = (
            By.XPATH,
            self.drop_down_menu_option_template.format(period=period)
        )
        self.driver.find_element(*selected_period).click()

    @allure.step('Выбираем дату аренды самоката')
    def set_rent_date(self, day):
        self.driver.find_element(*self.datepicker_input).click()
        self.wait_for_visibility_of_element_located(self.opened_datepicker)

        selected_date = (
            By.XPATH,
            self.datepicker_pick_day_template.format(day=day)
        )
        self.driver.find_element(*selected_date).click()
        self.wait_for_invisibility_of_element_located(self.opened_datepicker)
        self.driver.find_element(*self.final_order_button).click()
        self.wait_for_visibility_of_element_located(self.order_modal)

    @allure.step('Нажимаем кнопку Заказать')
    def make_order(self):
        self.driver.find_element(*self.button_yes).click()
        self.wait_for_visibility_of_element_located(self.order_modal__header)

        return self.driver.find_element(*self.order_modal__header).text

    @allure.step('Прокручиваем страницу вниз')
    def page_scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.wait_for_visibility_of_element_located(self.make_order__footer_button)

    @staticmethod
    @allure.step('Заполняем первую форму: имя, фамилия, адрес, станция метро и телефонный номер')
    def write_data_in_first_form(page, name, surname, address, station, number):
        page.set_name(name)
        page.set_surname(surname)
        page.set_address(address)
        page.set_metro_station(station)
        page.set_number(number)

        return page

    @staticmethod
    @allure.step('Заполняем вторую форму: период аренды и дата')
    def write_data_in_second_form(page, period, day):
        page.set_rent_period(period)
        page.set_rent_date(day)

        return page

    def click_scooter_logo(self):
        self.wait_for_visibility_of_element_located(self.scooter__header_link)
        self.driver.find_element(*self.scooter__header_link).click()

    def get_current_url(self):
        return self.driver.current_url

    def open_status_page(self):
        self.driver.find_element(*self.look_order_status).click()