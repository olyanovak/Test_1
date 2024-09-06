import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.radio_button.radio_button_methods import RadioButtonPage
from base.pages.radio_button.radio_button_methods import RadioButtonMethods


class RadioButtonStart:
    @staticmethod
    def radio_button(page: Page, radio_button: RadioButtonPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_radio_button(page)

            with allure.step("Нажатие на радио кнопку 'Yes'"):
                RadioButtonMethods.click_yes_radio(radio_button)

            with allure.step("Нажатие на радио кнопку 'Impressive'"):
                RadioButtonMethods.click_impressive_radio(radio_button)

        except AssertionError as e:
            errors.append(str(e))