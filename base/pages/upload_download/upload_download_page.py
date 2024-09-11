from playwright.sync_api import Page
from base.page_factory.button import Button
from base.page_factory.input import Input


class UploadDownloadPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Загрузить и скачать"""
        self.download_button = Button(page, locator='//*[@id="downloadButton"]', name='Скачать')
        self.upload_button = Input(page, locator='//*[@id="uploadFile"]', name='Загрузить')

        """Ожидания"""
        self.Wait_download_button= '//*[@id="downloadButton"]'
        self.Wait_upload_button = '//*[@id="uploadFile"]'



