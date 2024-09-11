import allure

from base.pages.text_box.text_box_page import TextBoxPage
from src.config.expectations import Wait


class TextBoxMethods:

    @staticmethod
    def fill_full_name_input(text_box: TextBoxPage):
        errors = []
        Wait.set_page(text_box.page)
        try:
            with allure.step("Ввод ФИО"):
                Wait.visible(text_box.Wait_full_name)
                text_box.full_name.fill(text_box.full_name_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_email_input(text_box: TextBoxPage):
        errors = []
        Wait.set_page(text_box.page)
        try:
            with allure.step("Ввод Email"):
                Wait.visible(text_box.Wait_email)
                text_box.email.fill(text_box.email_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_current_address_textarea(text_box: TextBoxPage):
        errors = []
        Wait.set_page(text_box.page)
        try:
            with allure.step("Ввод текущего адреса"):
                Wait.visible(text_box.Wait_current_address)
                text_box.current_address.fill_text(text_box.current_address_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_permanent_address_textarea(text_box: TextBoxPage):
        errors = []
        Wait.set_page(text_box.page)
        try:
            with allure.step("Ввод постоянного адреса"):
                Wait.visible(text_box.Wait_permanent_address)
                text_box.permanent_address.fill_text(text_box.permanent_address_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_submit(text_box: TextBoxPage):
        errors = []
        Wait.set_page(text_box.page)
        try:
            with allure.step("Отправка данных"):
                Wait.visible(text_box.Wait_submit)
                text_box.submit.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def screen_text_box(text_box: TextBoxPage):
        errors = []
        try:
            with allure.step("Скриншот страницы Text Box"):
                screenshot_path = f"screenshots/text_box_screen.png"
                text_box.page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, name='Заполнение полей и отправка данных',
                                   attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            errors.append(str(e))