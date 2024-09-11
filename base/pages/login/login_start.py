import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.login.login_page import LoginPage
from base.pages.login.login_methods import LoginMethods


class LoginStart:
    @staticmethod
    def login(page: Page, login: LoginPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_login(page)

            with allure.step("Ввод имени пользователя"):
                LoginMethods.fill_user_name(login)

            with allure.step("Ввод пароля"):
                LoginMethods.fill_password(login)

            with allure.step("Вход"):
                LoginMethods.click_login(login)

            with allure.step("Скриншот результата теста"):
                LoginMethods.screen_login(login)

        except AssertionError as e:
            errors.append(str(e))
