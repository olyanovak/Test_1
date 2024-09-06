from playwright.sync_api import Page
from base.page_factory.button import Button


class CheckBoxPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Флажок"""
        self.arrow_one = page.locator('(//*[starts-with(@aria-label, "Toggle")])[1]')
        self.arrow_two= page.locator('(//*[starts-with(@aria-label, "Toggle")])[2]')
        self.arrow_three = page.locator('(//*[starts-with(@aria-label, "Toggle")])[3]')
        self.arrow_four = page.locator('(//*[starts-with(@aria-label, "Toggle")])[4]')
        self.arrow_five = page.locator('(//*[starts-with(@aria-label, "Toggle")])[5]')
        self.arrow_six = page.locator('(//*[starts-with(@aria-label, "Toggle")])[6]')
        self.check_box_home = Button(page, locator='//*[@for="tree-node-home"]', name='Флажок папки Home')

        """Ожидания"""
        self.Wait_arrow_one = '(//*[starts-with(@aria-label, "Toggle")])[1]'
        self.Wait_arrow_two = '(//*[starts-with(@aria-label, "Toggle")])[2]'
        self.Wait_arrow_three = '(//*[starts-with(@aria-label, "Toggle")])[3]'
        self.Wait_arrow_four = '(//*[starts-with(@aria-label, "Toggle")])[4]'
        self.Wait_arrow_five = '(//*[starts-with(@aria-label, "Toggle")])[5]'
        self.Wait_arrow_six = '(//*[starts-with(@aria-label, "Toggle")])[6]'
        self.Wait_check_box_home = '//*[@for="tree-node-home"]'