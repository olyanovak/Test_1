from playwright.sync_api import Page
from base.page_factory.button import Button


class RadioButtonPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Радио кнопки"""
        self.yes_radio = Button(page, locator='//*[@for="yesRadio"]', name='Радио кнопка "Yes"')
        self.impressive_radio= Button(page, locator='//*[@for="impressiveRadio"]', name='Радио кнопка "Impressive"')
        self.no_radio = Button(page, locator='//*[@for="noRadio"]', name='Радио кнопка "No"')

        """Ожидания"""
        self.Wait_yes_radio = '//*[@for="yesRadio"]'
        self.Wait_impressive_radio = '//*[@for="impressiveRadio"]'
        self.Wait_no_radio = '//*[@for="noRadio"]'