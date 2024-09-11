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
        self.drop_month = Button(page,locator='//*[@id="dateOfBirthInput"]', name='Дата')
        self.next_month = Button(page, locator='//*[@aria-label="Next Month"]', name='Следующий месяц')
        self.twentieth_october = Button(page, locator='//*[@aria-label="Choose Sunday, October 20th, 2024"]', name='20 октября 2024')
        self.subjects = page.locator('//*[starts-with(@class, "subjects-auto-complete__value-container")]')
        self.hobbies1 = Button(page, locator='//*[@for="hobbies-checkbox-1"]', name='Спорт')
        self.hobbies2 = Button(page, locator='//*[@for="hobbies-checkbox-3"]', name='Музыка')
        self.upload_picture = Input(page, locator='//*[@id="uploadPicture"]', name='Загрузить')
        self.adress = TextArea(page, locator='//*[@id = "currentAddress"]', name='Адрес')
        self.select_state = Button(page, locator='//*[@id="state"]', name="Штат")
        self.state = page.get_by_text('Haryana').nth(1)
        self.select_city = Button(page, locator='//*[@id="city"]', name="Город")
        self.city = page.get_by_text('Panipat').nth(1)
        self.submit = Button(page, locator='//*[@id="submit"]', name='Отправить')

        """Ожидания"""
        self.Wait_first_name = '//*[@id="firstName"]'
        self.Wait_last_name = '//*[@id="lastName"]'
        self.Wait_e_mail = '//*[@id="userEmail"]'
        self.Wait_gender = '//*[@id="gender-radio-1"]'
        self.Wait_phone_number = '//*[@id="userNumber"]'
        self.Wait_drop_month = '//*[@id="dateOfBirthInput"]'
        self.Wait_next_month = '//*[@aria-label="Next Month"]'
        self.Wait_twentieth_october = '//*[@aria-label="Choose Sunday, October 20th, 2024"]'
        self.Wait_subjects = '//*[starts-with(@class, "subjects-auto-complete__value-container")]'
        self.Wait_hobbies1 = '//*[@for="hobbies-checkbox-1"]'
        self.Wait_hobbies2 = '//*[@for="hobbies-checkbox-3"]'
        self.Wait_upload_picture = '//*[@id="uploadPicture"]'
        self.Wait_adress = '//*[@id="currentAddress"]'
        self.Wait_select_state = '//*[@id="state"]'
        self.Wait_select_city = '//*[@id="city"]'
        self.Wait_submit = '//*[@id="submit"]'

        """Текст для ввода"""
        self.first_name_text = "Иван"
        self.last_name_text = "Иванов"
        self.e_mail_text = "ivan@example.com"
        self.phone_number_text = "1234567890"
        self.subjects_text = "Python, pytest, playwright, allure, pydantic, xpath"
        self.adress_text = "ул.Красная, 1"
