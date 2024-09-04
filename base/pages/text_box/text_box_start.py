import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.text_box.text_box_methods import TextBoxPage
from base.pages.text_box.text_box_methods import TextBoxMethods


class TextBoxStart:
    @staticmethod
    def text_box(page: Page, text_box: TextBoxPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_text_box(page)

            with allure.step("Ввод ФИО пользователя"):
                TextBoxMethods.fill_full_name_input(text_box)

            with allure.step("Ввод Email"):
                TextBoxMethods.fill_email_input(text_box)

            with allure.step("Ввод текущего адреса"):
                TextBoxMethods.fill_current_address_textarea(text_box)

            with allure.step("Ввод постоянного адреса"):
                TextBoxMethods.fill_permanent_address_textarea(text_box)

            with allure.step("Отправка данных"):
                TextBoxMethods.click_submit(text_box)

        except AssertionError as e:
            errors.append(str(e))