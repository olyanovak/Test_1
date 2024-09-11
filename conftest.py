import pytest

from playwright.sync_api import Page, sync_playwright, Browser

from base.pages.practice_form.practice_form_page import PracticeFormPage
from base.pages.radio_button.radio_button_page import RadioButtonPage
from base.pages.text_box.text_box_page import TextBoxPage
from base.pages.check_box.check_box_page import CheckBoxPage
from base.pages.buttons.buttons_page import ButtonsPage
from base.pages.upload_download.upload_download_page import UploadDownloadPage
from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from base.pages.date_picker.date_picker_page import DatePickerPage
from base.pages.select_menu.select_menu_page import SelectMenuPage
from base.pages.login.login_page import LoginPage
from src.config.playwright import PlaywrightConfig

@pytest.fixture()
def page() -> Page:
    with sync_playwright() as playwright:
        browser = get_browser(playwright)
        page = browser.new_page(viewport=PlaywrightConfig.PAGE_VIEWPORT_SIZE)
        yield page
        browser.close()

def get_browser(playwright) -> Browser:
    browser_type = playwright.chromium if PlaywrightConfig.BROWSER == 'chrome' else playwright.firefox
    return browser_type.launch(
        headless=PlaywrightConfig.IS_HEADLESS,
        slow_mo=PlaywrightConfig.SLOW_MO
    )


@pytest.fixture(scope='function')
def practice_form(page: Page) -> PracticeFormPage:
    return PracticeFormPage(page)

@pytest.fixture(scope='function')
def text_box(page: Page) -> TextBoxPage:
    return TextBoxPage(page)

@pytest.fixture(scope='function')
def check_box(page: Page) -> CheckBoxPage:
    return CheckBoxPage(page)

@pytest.fixture(scope='function')
def radio_button(page: Page) -> RadioButtonPage:
    return RadioButtonPage(page)

@pytest.fixture(scope='function')
def buttons(page: Page) -> ButtonsPage:
    return ButtonsPage(page)

@pytest.fixture(scope='function')
def upload_download(page: Page) -> UploadDownloadPage:
    return UploadDownloadPage(page)

@pytest.fixture(scope='function')
def modal_dialogs(page: Page) -> ModalDialogsPage:
    return ModalDialogsPage(page)

@pytest.fixture(scope='function')
def date_picker(page: Page) -> DatePickerPage:
    return DatePickerPage(page)

@pytest.fixture(scope='function')
def select_menu(page: Page) -> SelectMenuPage:
    return SelectMenuPage(page)

@pytest.fixture(scope='function')
def login(page: Page) -> LoginPage:
    return LoginPage(page)

