import allure

from base.pages.select_menu.select_menu_page import SelectMenuPage
from src.config.expectations import Wait


class SelectMenuMethods:

    @staticmethod
    def click_select_value(select_menu: SelectMenuPage):
        errors = []
        Wait.set_page(select_menu.page)
        try:
            with allure.step("Выбор значения"):
                Wait.visible(select_menu.Wait_select_group)
                select_menu.select_group.click()
                select_menu.group.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_select_one(select_menu: SelectMenuPage):
        errors = []
        Wait.set_page(select_menu.page)
        try:
            with allure.step("Выбор одного"):
                Wait.visible(select_menu.Wait_select_one)
                select_menu.select_one.click()
                select_menu.one.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def click_select_color(select_menu: SelectMenuPage):
        errors = []
        Wait.set_page(select_menu.page)
        try:
            with allure.step("Выбор цвета"):
                Wait.visible(select_menu.Wait_select_color)
                select_menu.select_color.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def screen_select_menu(select_menu: SelectMenuPage):
        errors = []
        try:
            with allure.step("Скриншот страницы Select Menu"):
                screenshot_path = f"screenshots/select_menu_screen.png"
                select_menu.page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, name='Выбор меню',
                                   attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            errors.append(str(e))
