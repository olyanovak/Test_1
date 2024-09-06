import allure

from base.pages.radio_button.radio_button_page import RadioButtonPage
from src.config.expectations import Wait


class RadioButtonMethods:

    @staticmethod
    def click_yes_radio(radio_button: RadioButtonPage):
        errors = []
        Wait.set_page(radio_button.page)
        try:
            with allure.step("Нажатие на радио кнопку 'Yes'"):
                Wait.visible(radio_button.Wait_yes_radio)
                radio_button.yes_radio.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_impressive_radio(radio_button: RadioButtonPage):
        errors = []
        Wait.set_page(radio_button.page)
        try:
            with allure.step("Нажатие на радио кнопку 'Impressive'"):
                Wait.visible(radio_button.Wait_impressive_radio)
                radio_button.impressive_radio.click()

        except AssertionError as e:
            errors.append(str(e))