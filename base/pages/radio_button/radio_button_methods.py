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

    @staticmethod
    def click_no_radio(radio_button: RadioButtonPage):
        errors = []
        Wait.set_page(radio_button.page)
        try:
            with allure.step("Проверка неактивности радио кнопки 'No'"):
                Wait.visible(radio_button.Wait_no_radio)
                radio_button.no_radio.should_be_disabled()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def screen_radio_button(radio_button: RadioButtonPage):
        errors = []
        try:
            with allure.step("Скриншот страницы Radio Button"):
                screenshot_path = f"screenshots/radio_button_screen.png"
                radio_button.page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, name='Нажатие на радио кнопку',
                                   attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            errors.append(str(e))