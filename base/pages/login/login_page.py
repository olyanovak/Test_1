from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Логин"""
        self.user_name = Input(page, locator='//*[@id="userName"]', name='UserName')
        self.password = Input(page, locator='//*[@id="password"]', name='Password')
        self.login_button = Button(page, locator='//*[@id="login"]', name='Login')

        """Ожидания"""
        self.Wait_user_name = '//*[@id="userName"]'
        self.Wait_password = '//*[@id="password"]'
        self.Wait_login_button = '//*[@id="login"]'

        """Текст для ввода"""
        self.user_name_text = "o.novak"
        self.password_text = "Olya.novak1!"
