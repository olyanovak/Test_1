from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input
from base.page_factory.textarea import TextArea


class TextBoxPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Текстовое поле"""
        self.full_name = Input(page, locator='//*[@id="userName"]', name='ФИО')
        self.email = Input(page, locator='//*[@id="userEmail"]', name='Email')
        self.current_address = TextArea(page, locator='//*[@id="currentAddress"]', name='Текущий адрес')
        self.permanent_address = TextArea(page, locator='//*[@id="permanentAddress"]', name='Постоянный адрес')
        self.submit = Button(page, locator='//*[@id="submit"]', name='Отправить')

        """Ожидания"""
        self.Wait_full_name = '//*[@id="userName"]'
        self.Wait_email = '//*[@id="userEmail"]'
        self.Wait_current_address = '//*[@id="currentAddress"]'
        self.Wait_permanent_address = '//*[@id="permanentAddress"]'
        self.Wait_submit = '//*[@id="submit"]'

        """Текст для ввода"""
        self.full_name_text = "Новак Ольга Павловна"
        self.email_text = "o.novak@digital.ru"
        self.current_address_text = "г. Краснодар, ул. Захарова, 11"
        self.permanent_address_text = "г. Краснодар, ул. Владимира Жириновского, 1"

