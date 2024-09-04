import time
from os import path

import allure
import page

from base.pages.text_box.text_box_page import TextBoxPage
from src.config.expectations import Wait


class TextBoxMethods:

    @staticmethod
    def fill_full_name_input(text_box: TextBoxPage):
        errors = []
        Wait.set_page(text_box.page)
        try:
            with allure.step("Ввод ФИО"):
                text_box.full_name.fill(text_box.full_name_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_email_input(text_box: TextBoxPage):
        errors = []
        Wait.set_page(text_box.page)
        try:
            with allure.step("Ввод Email"):
                text_box.email.fill(text_box.email_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_current_address_textarea(text_box: TextBoxPage):
        errors = []
        Wait.set_page(text_box.page)
        try:
            with allure.step("Ввод текущего адреса"):
                text_box.current_address.fill_text(text_box.current_address_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def fill_permanent_address_textarea(text_box: TextBoxPage):
        errors = []
        Wait.set_page(text_box.page)
        try:
            with allure.step("Ввод постоянного адреса"):
                text_box.permanent_address.fill_text(text_box.permanent_address_text)

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_submit(text_box: TextBoxPage):
        errors = []
        Wait.set_page(text_box.page)
        try:
            with allure.step("Отправка данных"):
                text_box.submit.click()

        except AssertionError as e:
            errors.append(str(e))