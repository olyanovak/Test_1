import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from base.pages.modal_dialogs.modal_dialogs_methods import ModalDialogsMethods


class ModalDialogsStart:
    @staticmethod
    def modal_dialogs(page: Page, modal_dialogs: ModalDialogsPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_modal_dialogs(page)

            with allure.step("Нажатие на кнопку открытия маленького модального диалога"):
                ModalDialogsMethods.open_small_modal(modal_dialogs)

            with allure.step("Скриншот маленького модального диалога"):
                ModalDialogsMethods.screen_modal_dialogs(modal_dialogs)

            with allure.step("Нажатие на кнопку закрытия маленького модального диалога"):
                ModalDialogsMethods.close_small_modal(modal_dialogs)

            with allure.step("Нажатие на кнопку открытия большого модального диалога"):
                ModalDialogsMethods.open_large_modal(modal_dialogs)

            with allure.step("Скриншот большого модального диалога"):
                ModalDialogsMethods.screen_modal_dialogs(modal_dialogs)

            with allure.step("Нажатие на кнопку закрытия большого модального диалога"):
                ModalDialogsMethods.close_large_modal(modal_dialogs)

        except AssertionError as e:
            errors.append(str(e))