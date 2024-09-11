import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.select_menu.select_menu_methods import SelectMenuMethods
from base.pages.select_menu.select_menu_page import SelectMenuPage


class SelectMenuStart:
    @staticmethod
    def select_menu(page: Page, select_menu: SelectMenuPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_select_menu(page)

            with allure.step("Выбор группы"):
                SelectMenuMethods.click_select_value(select_menu)

            with allure.step("Выбор одного"):
                SelectMenuMethods.click_select_one(select_menu)

            with allure.step("Выбор цвета"):
                SelectMenuMethods.click_select_color(select_menu)

            with allure.step("Скриншот результата теста"):
                SelectMenuMethods.screen_select_menu(select_menu)

        except AssertionError as e:
            errors.append(str(e))
