from playwright.sync_api import Page

from base.page_factory.button import Button


class SelectMenuPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Выбор меню"""
        self.select_group = Button(page,locator='//*[@id="withOptGroup"]',name="Группа")
        self.group = page.get_by_text('Group 1, option 1').nth(1)
        self.select_one = Button(page,locator='//*[@id="selectOne"]',name="Один")
        self.one = page.get_by_text('Mrs.')
        self.select_color = Button(page,locator='//*[@id="oldSelectMenu"]', name="Цвет")


        """Ожидания"""
        self.Wait_select_group= '//*[@id="withOptGroup"]'
        self.Wait_select_one = '//*[@id="selectOne"]'
        self.Wait_select_color = '//*[@id="oldSelectMenu"]'

