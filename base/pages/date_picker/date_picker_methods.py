import allure

from base.pages.date_picker.date_picker_page import DatePickerPage
from src.config.expectations import Wait


class DatePickerMethods:

    @staticmethod
    def click_select_date(date_picker: DatePickerPage):
        errors = []
        Wait.set_page(date_picker.page)
        try:
            with allure.step("Выбор даты 20 октября 2024"):
                Wait.visible(date_picker.Wait_select_date)
                date_picker.select_date.click()
                Wait.visible(date_picker.Wait_next_month)
                date_picker.next_month.click()
                Wait.visible(date_picker.Wait_twentieth_october)
                date_picker.twentieth_october.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_date_and_time(date_picker: DatePickerPage):
        errors = []
        Wait.set_page(date_picker.page)
        try:
            with allure.step("Выбор даты 20 октября 2024 и времени 22:00"):
                Wait.visible(date_picker.Wait_date_and_time)
                date_picker.date_and_time.click()
                Wait.visible(date_picker.Wait_next_month)
                date_picker.next_month.click()
                Wait.visible(date_picker.Wait_twentieth_october)
                date_picker.twentieth_october.click()
                date_picker.time_ten_pm.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def screen_date_picker(date_picker: DatePickerPage):
        errors = []
        try:
            with allure.step("Скриншот страницы Date Picker"):
                screenshot_path = f"screenshots/date_picker_screen.png"
                date_picker.page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, name='Выбор даты и времени',
                                   attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            errors.append(str(e))
