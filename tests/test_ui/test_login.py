import allure
from playwright.sync_api import Page

from base.pages.login.login_page import LoginPage
from base.pages.login.login_start import LoginStart
from conftest import login


class TestLogin:

    @allure.epic("UI")
    @allure.feature("Login")
    @allure.title("Авторизация")
    def test_login(self, page: Page, login: LoginPage):
        LoginStart.login(page, login)