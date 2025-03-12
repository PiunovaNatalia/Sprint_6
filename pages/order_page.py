from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage


class OrderPage(BasePage):
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
        super(OrderPage, self).__init__(driver)

    @allure.step('Ищем кнопку для совершения заказа в шапке сайта')
    def get_make_order_header_button(self):
        return self.get_element(self.make_order__header_button)

    @allure.step('Ищем кнопку для совершения заказа внизу страницы сайта')
    def get_make_order_footer_button(self):
        return self.get_element(self.make_order__footer_button)

    @allure.step('Вводим имя')
    def set_name(self, name):
        self.get_element(self.name_input).send_keys(name)

    @allure.step('Вводим фамилию')
    def set_surname(self, surname):
        self.get_element(self.surname_input).send_keys(surname)

    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.get_element(self.address_input).send_keys(address)

    @allure.step('Выбираем станцию метро')
    def set_metro_station(self, metro_station):
        self.click(self.metro_station_input)
        self.wait_for_visibility_of_element(self.select_input)

        selected_station = (
            By.XPATH,
            self.selected_station_template.format(metro_station=metro_station)
        )
        self.get_element(selected_station).click()

        self.wait_for_invisibility_of_element(self.select_input)

    @allure.step('Вводим номер телефона')
    def set_number(self, number):
        self.get_element(self.number_input).send_keys(number)

    @allure.step('Нажимаем кнопку Далее')
    def go_to_next_form(self):
        self.click(self.button_next)
        self.wait_for_visibility_of_element(self.header_about_rent)

    @allure.step('Выбираем период аренды самоката')
    def set_rent_period(self, period):
        self.click(self.rent_time_button)
        self.wait_for_visibility_of_element(self.drop_down_menu)
        selected_period = (By.XPATH, self.drop_down_menu_option_template.format(period=period))
        self.click(selected_period)

    @allure.step('Выбираем дату аренды самоката')
    def set_rent_date(self, day):
        self.click(self.datepicker_input)
        self.wait_for_visibility_of_element(self.opened_datepicker)

        selected_date = (
            By.XPATH,
            self.datepicker_pick_day_template.format(day=day)
        )
        self.click(selected_date)
        self.wait_for_invisibility_of_element(self.opened_datepicker)
        self.click(self.final_order_button)
        self.wait_for_visibility_of_element(self.order_modal)

    @allure.step('Нажимаем кнопку Заказать')
    def make_order(self):
        self.click(self.button_yes)
        self.wait_for_visibility_of_element(self.order_modal__header)

        return self.get_element(self.order_modal__header).text

    @allure.step('Заполняем первую форму: имя, фамилия, адрес, станция метро и телефонный номер')
    def write_data_in_first_form(self, name, surname, address, station, number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station(station)
        self.set_number(number)

    @allure.step('Заполняем вторую форму: период аренды и дата')
    def write_data_in_second_form(self, period, day):
        self.set_rent_period(period)
        self.set_rent_date(day)

    @allure.step('Нажимаем на логотип Самокат')
    def click_scooter_logo(self):
        self.click(self.scooter__header_link)

    @allure.step('Открываем страницу статуса заказа')
    def open_status_page(self):
        self.click(self.look_order_status)
        self.wait_for_visibility_of_element(self.scooter__header_link)