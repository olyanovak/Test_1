import allure

from base.pages.buttons.buttons_page import ButtonsPage
from src.config.expectations import Wait


class ButtonsMethods:

    @staticmethod
    def double_click_me(buttons: ButtonsPage):
        errors = []
        Wait.set_page(buttons.page)
        try:
            with allure.step("Двойной клик"):
                Wait.visible(buttons.Wait_double_click_button)
                buttons.double_click_button.double_click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def right_click_me(buttons: ButtonsPage):
        errors = []
        Wait.set_page(buttons.page)
        try:
            with allure.step("Правый клик"):
                Wait.visible(buttons.Wait_right_click_button)
                buttons.right_click_button.r_click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_me(buttons: ButtonsPage):
        errors = []
        Wait.set_page(buttons.page)
        try:
            with allure.step("Простой клик"):
                Wait.visible(buttons.Wait_dynamic_click_button)
                buttons.dynamic_click_button.nth(2).click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def screen_buttons(buttons: ButtonsPage):
        errors = []
        try:
            with allure.step("Скриншот страницы Buttons"):
                screenshot_path = f"screenshots/buttons_screen.png"
                buttons.page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, name='Нажатие кнопок',
                                   attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            errors.append(str(e))