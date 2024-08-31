import time
from os import path

import allure

from base.pages.practice_form.practice_form_page import PracticeFormPage
#from src.config.expectations import Wait


class PracticeFormMethods:

    @staticmethod
    def fill_info_user_input(practice_form: PracticeFormPage):
        errors = []
        #Wait.set_page(practice_form.page)
        try:
            with allure.step("Ввод имени и фамилии"):
                practice_form.first_name.fill(practice_form.first_name_text)
                practice_form.last_name.fill(practice_form.last_name_text)
            with allure.step("Ввод Email"):
                practice_form.e_mail.fill(practice_form.e_mail_text)
            with allure.step("Выбор пола"):
                practice_form.gender.click()
            with allure.step("Ввод номера телефона"):
                practice_form.phone_number.fill(practice_form.phone_number_text)
            #with allure.step("Выбор даты"):
                #practice_form.drop_month.nth(1).click()
                #Wait.visible(practice_form.Wait_drop_month)
            with allure.step("Ввод предметов"):
                practice_form.subjects.click()
                practice_form.subjects.focus()
                practice_form.page.keyboard.type(practice_form.subjects_text , delay=1)

            #with allure.step("Выбор хобби"):
                #practice_form.hobbies.nth(0).click()

            with allure.step("Ввод текущего адреса"):
                practice_form.adress.fill_text(practice_form.adress_text)

            #with allure.step("Выбор штата"):
                #practice_form.state.click()
                #practice_form.state.focus()
                #practice_form.page.keyboard.type(practice_form.state_text, delay=1)

            #with allure.step("Выбор города"):
                #practice_form.city.focus()
                #practice_form.city.click()

            with allure.step("Отправить"):
                practice_form.submit.click()
            practice_form.page.screenshot(path='src/img/screen.png')

            time.sleep(20)



        except AssertionError as e:
            errors.append(str(e))