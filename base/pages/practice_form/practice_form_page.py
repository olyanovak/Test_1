from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input
from base.page_factory.textarea import TextArea


class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Форма"""
        self.first_name = Input(page, locator='//*[@id="firstName"]', name='Имя')
        self.last_name = Input(page, locator='//*[@id="lastName"]', name='Фамилия')
        self.e_mail = Input(page, locator='//*[@id="userEmail"]', name='E-mail')
        self.gender = Button(page, locator='//*[@for="gender-radio-1"]', name='Пол')
        self.phone_number = Input(page, locator='//*[@id="userNumber"]', name='Номер телефона')
        # self.drop_month = page.locator('//*[starts-with(@class, "react-datepicker__month")]')
        self.subjects = page.locator('//*[starts-with(@class, "subjects-auto-complete__value-container")]')
        # self.hobbies = Button(page, locator='//*[@id="hobbies-checkbox-1"]', name='Хобби')
        # self.hobbies = page.locator('(//*[starts-with(@class, "custom-control custom-checkbox")])[0]')
        self.adress = TextArea(page, locator='//*[@id = "currentAddress"]', name='Адрес')
        # self.state = Button(page,locator='//*[@id="state"]', name="Штат")
        # self.city = Button(page, locator='//*[@id="city"]', name="Город")
        self.submit = Button(page, locator='//*[@id="submit"]', name='Отправить')

        """Ожидания"""
        self.Wait_first_name = '//*[@id="firstName"]'
        self.Wait_last_name = '//*[@id="lastName"]'
        self.Wait_e_mail = '//*[@id="userEmail"]'
        self.Wait_gender = '//*[@id="gender-radio-1"]'
        self.Wait_phone_number = '//*[@id="userNumber"]'
        # self.Wait_drop_month = '(//*[starts-with(@class, "react-datepicker__month")])[2]'
        self.Wait_subjects = '//*[starts-with(@class, "subjects-auto-complete__value-container")]'
        # self.Wait_hobbies = '(//*[starts-with(@class, "custom-control custom-checkbox")])[0]'
        self.Wait_adress = '//*[@id="currentAddress"]'
        self.Wait_state = '//*[@id="state"]'
        self.Wait_city = '//*[@id="city"]'
        self.Wait_submit = '//*[@id="submit"]'

        """Текст для ввода"""
        self.first_name_text = "Иван"
        self.last_name_text = "Иванов"
        self.e_mail_text = "ivan@example.com"
        self.phone_number_text = "1234567890"
        self.subjects_text = "Python, pytest, playwright, allure, pydantic, xpath"
        self.adress_text = "ул.Красная, 1"
        # self.state_text = "Haryana"
        # self.city_text = "Panipat"
