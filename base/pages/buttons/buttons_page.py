from playwright.sync_api import Page
from base.page_factory.button import Button


class ButtonsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Кнопки"""
        self.double_click_button = Button(page, locator='//*[@id="doubleClickBtn"]', name='Двойной клик')
        self.right_click_button= Button(page, locator='//*[@id="rightClickBtn"]', name='Правый клик')
        self.dynamic_click_button = page.locator('(//*[@class="btn btn-primary"])')

        """Ожидания"""
        self.Wait_double_click_button = '//*[@id="doubleClickBtn"]'
        self.Wait_right_click_button = '//*[@id="rightClickBtn"]'
        self.Wait_dynamic_click_button = '(//*[@class="btn btn-primary"])[3]'