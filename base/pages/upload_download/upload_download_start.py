import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.upload_download.upload_download_page import UploadDownloadPage
from base.pages.upload_download.upload_download_methods import UploadDownloadMethods


class UploadDownloadStart:
    @staticmethod
    def upload_download(page: Page, upload_download: UploadDownloadPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_upload_download(page)

            with allure.step("Нажатие на кнопку скачивания файла"):
                UploadDownloadMethods.download_sample_file(upload_download)

            with allure.step("Скриншот результата скачивания файла"):
                UploadDownloadMethods.screen_upload_download(upload_download)

            with allure.step("Загрузка файла"):
                UploadDownloadMethods.upload(upload_download)

            with allure.step("Скриншот результата загрузки файла"):
                UploadDownloadMethods.screen_upload_download(upload_download)

        except AssertionError as e:
            errors.append(str(e))