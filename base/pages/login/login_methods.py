import allure

from base.pages.login.login_page import LoginPage
from src.config.expectations import Wait


class LoginMethods:

    @staticmethod
    def fill_user_name(login: LoginPage):
        errors = []
        Wait.set_page(login.page)
        try:
            with allure.step("Ввод имени пользователя"):
                Wait.visible(login.Wait_user_name)
                login.user_name.fill(login.user_name_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_password(login: LoginPage):
        errors = []
        Wait.set_page(login.page)
        try:
            with allure.step("Ввод пароля"):
                Wait.visible(login.Wait_password)
                login.password.fill(login.password_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_login(login: LoginPage):
        errors = []
        Wait.set_page(login.page)
        try:
            with allure.step("Войти"):
                Wait.visible(login.Wait_login_button)
                login.login_button.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def screen_login(login: LoginPage):
        errors = []
        try:
            with allure.step("Скриншот страницы Login"):
                screenshot_path = f"screenshots/login_screen.png"
                login.page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, name='Авторизация',
                                   attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            errors.append(str(e))