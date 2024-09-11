from playwright.sync_api import Page
from base.page_factory.button import Button


class ModalDialogsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Модальные диалоги"""
        self.small_modal = Button(page, locator='//*[@id="showSmallModal"]', name='Маленький модальный диалог')
        self.small_close = Button(page, locator='//*[@id="closeSmallModal"]', name='Закрыть маленький модальный диалог')
        self.large_modal = Button(page, locator='//*[@id="showLargeModal"]', name='Большой модальный диалог')
        self.large_close = Button(page, locator='//*[@id="closeLargeModal"]', name='Закрыть большой модальный диалог')

        """Ожидания"""
        self.Wait_small_modal= '//*[@id="showSmallModal"]'
        self.Wait_small_close = '//*[@id="closeSmallModal"]'
        self.Wait_large_modal = '//*[@id="showLargeModal"]'
        self.Wait_large_close = '//*[@id="closeLargeModal"]'

