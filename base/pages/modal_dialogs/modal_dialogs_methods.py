import allure

from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from src.config.expectations import Wait


class ModalDialogsMethods:

    @staticmethod
    def open_small_modal(modal_dialogs: ModalDialogsPage):
        errors = []
        Wait.set_page(modal_dialogs.page)
        try:
            with allure.step("Открытие маленького модального диалога"):
                Wait.visible(modal_dialogs.Wait_small_modal)
                modal_dialogs.small_modal.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def close_small_modal(modal_dialogs: ModalDialogsPage):
        errors = []
        Wait.set_page(modal_dialogs.page)
        try:
            with allure.step("Закрытие маленького модального диалога"):
                Wait.visible(modal_dialogs.Wait_small_close)
                modal_dialogs.small_close.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def open_large_modal(modal_dialogs: ModalDialogsPage):
        errors = []
        Wait.set_page(modal_dialogs.page)
        try:
            with allure.step("Открытие большого модального диалога"):
                Wait.visible(modal_dialogs.Wait_large_modal)
                modal_dialogs.large_modal.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def close_large_modal(modal_dialogs: ModalDialogsPage):
        errors = []
        Wait.set_page(modal_dialogs.page)
        try:
            with allure.step("Закрытие большого модального диалога"):
                Wait.visible(modal_dialogs.Wait_large_close)
                modal_dialogs.large_close.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def screen_modal_dialogs(modal_dialogs: ModalDialogsPage):
        errors = []
        try:
            with allure.step("Скриншот страницы Modal Dialogs"):
                screenshot_path = f"screenshots/modal_dialogs_screen.png"
                modal_dialogs.page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, name='Модальный диалог',
                                   attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            errors.append(str(e))
