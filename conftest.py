import pytest
from playwright.sync_api import Page, sync_playwright, Browser

from base.pages.practice_form.practice_form_page import PracticeFormPage
from src import config

@pytest.fixture()
def page() -> Page:
    with sync_playwright() as playwright:
        browser = get_browser(playwright)
        page = browser.new_page()
        yield page
        browser.close()


def get_browser(playwright) -> Browser:
    browser_type = playwright.chromium if config.playwright.BROWSER == 'chrome' else playwright.firefox
    return browser_type.launch(
        headless=config.playwright.IS_HEADLESS,
        slow_mo=config.playwright.SLOW_MO
    )


@pytest.fixture(scope='function')
def practice_form(page: Page) -> PracticeFormPage:
    return PracticeFormPage(page)