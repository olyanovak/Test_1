import allure
from playwright.sync_api import Page

from base.pages.radio_button.radio_button_page import RadioButtonPage
from base.pages.radio_button.radio_button_start import RadioButtonStart
from conftest import radio_button


class TestRadioButton:

    @allure.epic("UI")
    @allure.feature("Radio Button")
    @allure.title("Нажатие на радио кнопки")
    def test_radio_button(self, page: Page, radio_button: RadioButtonPage):
        RadioButtonStart.radio_button(page, radio_button)