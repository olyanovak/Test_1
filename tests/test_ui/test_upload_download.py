import allure
from playwright.sync_api import Page

from base.pages.upload_download.upload_download_page import UploadDownloadPage
from base.pages.upload_download.upload_download_start import UploadDownloadStart
from conftest import upload_download


class TestUploadDownload:

    @allure.epic("UI")
    @allure.feature("Upload and Download")
    @allure.title("Загрузка и скачивание файлов")
    def test_upload_download(self, page: Page, upload_download: UploadDownloadPage):
        UploadDownloadStart.upload_download(page, upload_download)