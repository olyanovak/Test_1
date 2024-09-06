import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.check_box.check_box_methods import CheckBoxPage
from base.pages.check_box.check_box_methods import CheckBoxMethods


class CheckBoxStart:
    @staticmethod
    def check_box(page: Page, check_box: CheckBoxPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_check_box(page)

            with allure.step("Нажатие на стрелку 1"):
                CheckBoxMethods.click_arrow_one(check_box)

            with allure.step("Нажатие на стрелку 2"):
                CheckBoxMethods.click_arrow_two(check_box)

            with allure.step("Нажатие на стрелку 3"):
                CheckBoxMethods.click_arrow_three(check_box)

            with allure.step("Нажатие на стрелку 4"):
                CheckBoxMethods.click_arrow_four(check_box)

            with allure.step("Нажатие на стрелку 5"):
                CheckBoxMethods.click_arrow_five(check_box)

            with allure.step("Нажатие на стрелку 6"):
                CheckBoxMethods.click_arrow_six(check_box)

            with allure.step("Нажатие на флажок папки Home"):
                CheckBoxMethods.click_check_box_home(check_box)

        except AssertionError as e:
            errors.append(str(e))