import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.practice_form.practice_form_methods import PracticeFormMethods
from base.pages.practice_form.practice_form_page import PracticeFormPage


class PracticeStart:
    @staticmethod
    def practice_form(page: Page, practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_practice_form(page)

            with allure.step("Ввод данных пользователя"):
                PracticeFormMethods.fill_info_user(practice_form)

            with allure.step("Ввод Email"):
                PracticeFormMethods.fill_e_mail(practice_form)

            with allure.step("Выбор пола"):
                PracticeFormMethods.click_gender(practice_form)

            with allure.step("Ввод номера телефона"):
                PracticeFormMethods.fill_phone_number(practice_form)

            with allure.step("Выбор даты"):
                PracticeFormMethods.click_drop_month(practice_form)

            with allure.step("Ввод предметов"):
                PracticeFormMethods.fill_subjects(practice_form)

            with allure.step("Выбор хобби"):
                PracticeFormMethods.click_hobbies(practice_form)

            with allure.step("Загрузка файла"):
                PracticeFormMethods.load_picture(practice_form)

            with allure.step("Ввод текущего адреса"):
                PracticeFormMethods.fill_adress(practice_form)

            with allure.step("Выбор штата"):
                PracticeFormMethods.click_select_state(practice_form)

            with allure.step("Выбор города"):
                PracticeFormMethods.click_select_city(practice_form)

            with allure.step("Отправить"):
                PracticeFormMethods.click_submit(practice_form)

            with allure.step("Скриншот результата теста"):
                PracticeFormMethods.screen_practice_form(practice_form)

        except AssertionError as e:
            errors.append(str(e))