import allure

from base.pages.practice_form.practice_form_page import PracticeFormPage
from src.config.expectations import Wait


class PracticeFormMethods:

    @staticmethod
    def fill_name_input(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Ввод имени и фамилии"):
                #Wait.visible(practice_form.Wait_first_name)
                practice_form.first_name.fill("Иван")

                #Wait.visible(practice_form.Wait_last_name)
                practice_form.last_name.fill("Иванов")

        except AssertionError as e:
            errors.append(str(e))