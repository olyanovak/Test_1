from playwright.sync_api import Page
from base.page_factory.button import Button


class DatePickerPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Выбор даты"""
        self.select_date = Button(page, locator='//*[@id="datePickerMonthYearInput"]', name='Дата')
        self.next_month = Button(page, locator='//*[@aria-label="Next Month"]', name='Следующий месяц')
        self.twentieth_october = Button(page, locator='//*[@aria-label="Choose Sunday, October 20th, 2024"]', name='20 октября 2024')
        self.date_and_time = Button(page, locator='//*[@id="dateAndTimePickerInput"]', name='Дата и время')
        self.time_ten_pm = page.get_by_text('22:00')

        """Ожидания"""
        self.Wait_select_date= '//*[@id="datePickerMonthYearInput"]'
        self.Wait_next_month = '//*[@aria-label="Next Month"]'
        self.Wait_twentieth_october = '//*[@aria-label="Choose Sunday, October 20th, 2024"]'
        self.Wait_date_and_time = '//*[@id="dateAndTimePickerInput"]'

