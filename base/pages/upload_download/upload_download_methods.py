import allure

from base.pages.upload_download.upload_download_page import UploadDownloadPage
from src.config.expectations import Wait


class UploadDownloadMethods:

    @staticmethod
    def download_sample_file(upload_download: UploadDownloadPage):
        errors = []
        Wait.set_page(upload_download.page)
        try:
            with allure.step("Скачивание файла"):
                Wait.visible(upload_download.Wait_download_button)
                upload_download.download_button.click()

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def upload(upload_download: UploadDownloadPage):
        errors = []
        Wait.set_page(upload_download.page)
        try:
            with allure.step("Загрузка файла"):
                Wait.visible(upload_download.Wait_upload_button)
                upload_download.upload_button.load_file(path_file='src/img/sampleFile.jpeg')

        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def screen_upload_download(upload_download: UploadDownloadPage):
        errors = []
        try:
            with allure.step("Скриншот страницы Upload and Download"):
                screenshot_path = f"screenshots/upload_download_screen.png"
                upload_download.page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, name='Скачивание и загрузка файла',
                                   attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            errors.append(str(e))
