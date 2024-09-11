import allure
from playwright.sync_api import Page

from base.pages.select_menu.select_menu_page import SelectMenuPage
from base.pages.select_menu.select_menu_start import SelectMenuStart
from conftest import select_menu


class TestSelectMenu:

    @allure.epic("UI")
    @allure.feature("Select Menu")
    @allure.title("Выбор меню")
    def test_select_menu(self, page: Page, select_menu: SelectMenuPage):
        SelectMenuStart.select_menu(page, select_menu)