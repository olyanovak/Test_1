import allure

from base.pages.check_box.check_box_page import CheckBoxPage
from src.config.expectations import Wait


class CheckBoxMethods:

    @staticmethod
    def click_arrow_one(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Нажатие на стрелку 1"):
                Wait.visible(check_box.Wait_arrow_one)
                check_box.arrow_one.nth(0).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_arrow_two(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Нажатие на стрелку 2"):
                Wait.visible(check_box.Wait_arrow_two)
                check_box.arrow_two.nth(0).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_arrow_three(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Нажатие на стрелку 3"):
                Wait.visible(check_box.Wait_arrow_three)
                check_box.arrow_three.nth(0).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_arrow_four(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Нажатие на стрелку 4"):
                Wait.visible(check_box.Wait_arrow_four)
                check_box.arrow_four.nth(0).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_arrow_five(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Нажатие на стрелку 5"):
                Wait.visible(check_box.Wait_arrow_five)
                check_box.arrow_five.nth(0).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_arrow_six(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Нажатие на стрелку 6"):
                Wait.visible(check_box.Wait_arrow_six)
                check_box.arrow_six.nth(0).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_check_box_home(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Нажатие на флажок папки Home"):
                Wait.visible(check_box.Wait_check_box_home)
                check_box.check_box_home.click()

        except AssertionError as e:
            errors.append(str(e))