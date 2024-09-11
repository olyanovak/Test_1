import allure

from base.pages.practice_form.practice_form_page import PracticeFormPage
from src.config.expectations import Wait


class PracticeFormMethods:

    @staticmethod
    def fill_info_user(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Ввод имени и фамилии"):
                Wait.visible(practice_form.Wait_first_name)
                practice_form.first_name.fill(practice_form.first_name_text)
                Wait.visible(practice_form.Wait_last_name)
                practice_form.last_name.fill(practice_form.last_name_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_e_mail(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Ввод Email"):
                Wait.visible(practice_form.Wait_e_mail)
                practice_form.e_mail.fill(practice_form.e_mail_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_gender(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Выбор пола"):
                Wait.visible(practice_form.Wait_gender)
                practice_form.gender.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_phone_number(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Ввод номера телефона"):
                Wait.visible(practice_form.Wait_phone_number)
                practice_form.phone_number.fill(practice_form.phone_number_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_drop_month(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Выбор даты"):
                Wait.visible(practice_form.Wait_drop_month)
                practice_form.drop_month.click()
                Wait.visible(practice_form.Wait_next_month)
                practice_form.next_month.click()
                Wait.visible(practice_form.Wait_twentieth_october)
                practice_form.twentieth_october.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_subjects(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Ввод предметов"):
                Wait.visible(practice_form.Wait_subjects)
                practice_form.subjects.click()
                practice_form.subjects.focus()
                practice_form.page.keyboard.type(practice_form.subjects_text, delay=1)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_hobbies(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Выбор хобби"):
                Wait.visible(practice_form.Wait_hobbies1)
                practice_form.hobbies1.click()
                Wait.visible(practice_form.Wait_hobbies2)
                practice_form.hobbies2.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def load_picture(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Загрузка файла"):
                Wait.visible(practice_form.Wait_upload_picture)
                practice_form.upload_picture.load_file(path_file='src/img/sampleFile.jpeg')

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_adress(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Ввод текущего адреса"):
                Wait.visible(practice_form.Wait_adress)
                practice_form.adress.fill_text(practice_form.adress_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_select_state(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Выбор штата"):
                Wait.visible(practice_form.Wait_select_state)
                practice_form.select_state.click()
                practice_form.state.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_select_city(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Выбор города"):
                Wait.visible(practice_form.Wait_select_city)
                practice_form.select_city.click()
                practice_form.city.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_submit(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Отправить"):
                Wait.visible(practice_form.Wait_submit)
                practice_form.submit.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def screen_practice_form(practice_form: PracticeFormPage):
        errors = []
        try:
            with allure.step("Скриншот страницы Practice Form"):
                screenshot_path = f"screenshots/practice_form_screen.png"
                practice_form.page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, name='Заполнение формы',
                                   attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            errors.append(str(e))