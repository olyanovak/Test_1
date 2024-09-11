import allure
from playwright.sync_api import Page

from base.pages.date_picker.date_picker_page import DatePickerPage
from base.pages.date_picker.date_picker_start import DatePickerStart
from conftest import date_picker


class TestDatePicker:

    @allure.epic("UI")
    @allure.feature("Date Picker")
    @allure.title("Выбор даты")
    def test_date_picker(self, page: Page, date_picker: DatePickerPage):
        DatePickerStart.date_picker(page, date_picker)