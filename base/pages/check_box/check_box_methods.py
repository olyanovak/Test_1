import allure

from base.pages.check_box.check_box_page import CheckBoxPage
from src.config.expectations import Wait


class CheckBoxMethods:

    @staticmethod
    def click_arrow_one(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Cтрелка 1"):
                Wait.visible(check_box.Wait_arrow_one)
                check_box.arrow_one.nth(0).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_arrow_two(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Cтрелка 2"):
                Wait.visible(check_box.Wait_arrow_two)
                check_box.arrow_two.nth(1).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_arrow_three(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Cтрелка 3"):
                Wait.visible(check_box.Wait_arrow_three)
                check_box.arrow_three.nth(2).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_arrow_four(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Cтрелка 4"):
                Wait.visible(check_box.Wait_arrow_four)
                check_box.arrow_four.nth(3).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_arrow_five(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Cтрелка 5"):
                Wait.visible(check_box.Wait_arrow_five)
                check_box.arrow_five.nth(4).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_arrow_six(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Cтрелка 6"):
                Wait.visible(check_box.Wait_arrow_six)
                check_box.arrow_six.nth(5).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_check_box_home(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Флажок на папке Home"):
                Wait.visible(check_box.Wait_check_box_home)
                check_box.check_box_home.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def screen_check_box(check_box: CheckBoxPage):
        errors = []
        try:
            with allure.step("Скриншот страницы Check Box"):
                screenshot_path = f"screenshots/check_box_screen.png"
                check_box.page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, name='Флажки на всех папках',
                                   attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            errors.append(str(e))