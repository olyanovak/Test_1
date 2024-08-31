import allure
from playwright.sync_api import expect

from base.page_factory.component import Component
from settings import BASE_DIR


class TextArea(Component):
    @property
    def type_of(self) -> str:
        return 'текстовое поле'

    def fill_text(self, value: str, validate_value=False, **kwargs):
        """
        Заполняет текстовое поле текстом.
        """
        with allure.step(f'Заполнение {self.type_of} "{self.name}" значением "{value}"'):
            self.should_be_visible()
            locator = self.get_locator(**kwargs)
            locator.click()
            locator.fill(value)

    def unfocused(self, **kwargs):
        """
        Снимает фокус с текстового поля.
        """
        with allure.step(f'Снятие фокуса с текстового поля {self.name}'):
            locator = self.get_locator(**kwargs)
            locator.press("Tab")

    def should_have_value(self, value: str, **kwargs):
        """
        Проверяет, что текстовое поле имеет заданное значение.
        """
        with allure.step(f'Проверка, что {self.type_of} "{self.name}" имеет значение "{value}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_value(value)

    def load_file(self, path_file: str, **kwargs):
        """
        Загружает файл в текстовое поле (если поддерживается).
        """
        self.should_be_visible()
        with self.page.expect_file_chooser() as fc_info:
            self.get_locator(**kwargs).click()
        file_chooser = fc_info.value
        file_chooser.set_files(BASE_DIR + path_file, **kwargs)

    def hover(self, **kwargs) -> None:
        """
        Наводит курсор на текстовое поле.
        """
        with allure.step(f'Наведение курсора на {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.hover()