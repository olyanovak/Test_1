import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.buttons.buttons_page import ButtonsPage
from base.pages.buttons.buttons_methods import ButtonsMethods


class ButtonsStart:
    @staticmethod
    def buttons(page: Page, buttons: ButtonsPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_buttons(page)

            with allure.step("Нажатие на кнопку 'Double Click Me'"):
                ButtonsMethods.double_click_me(buttons)

            with allure.step("Нажатие на кнопку 'Right Click Me'"):
                ButtonsMethods.right_click_me(buttons)

            with allure.step("Нажатие на кнопку 'Click Me'"):
                ButtonsMethods.click_me(buttons)

            with allure.step("Скриншот результата"):
                ButtonsMethods.screen_buttons(buttons)

        except AssertionError as e:
            errors.append(str(e))