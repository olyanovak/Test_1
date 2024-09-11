import allure
from base.pages.api_pages.authorized.auth_base import AuthBase


class MethodsAuthorized:

    @staticmethod
    @allure.step("Авторизация пользователя через POST /Account/v1/Authorized")
    def post_v1_account_authorized():
        """
        Метод для выполнения авторизации пользователя через POST-запрос на эндпоинт /Account/v1/Authorized.

        Этот метод используется для авторизации пользователя, используя предоставленные имя пользователя и пароль.
        В процессе выполнения метода происходит несколько шагов:

        1. Создается экземпляр класса `AuthBase`, где задаются параметры авторизации (имя пользователя и пароль).
        2. Формируются данные для запроса и полный URL для авторизации.
        3. Выполняется отправка POST-запроса на сервер с предоставленными данными.
        4. Выполняется валидация ответа сервера, проверяется успешность авторизации.

        В случае успешной авторизации, результат валидации добавляется в отчет Allure и выводится в консоль.
        Если авторизация не удалась, тест завершится с ошибкой, и информация об этом также будет включена в отчет Allure.
        """
        auth_base = AuthBase(username="MakeyStar", password="23MakeyStar23!/")

        with allure.step("Формирование данных и отправка запроса"):
            data, url = auth_base.form_request_data(auth_base.get_authorized_endpoint())
            response = auth_base.send_post_request(data, url)

        with allure.step("Валидация ответа"):
            auth_base.validate_response(response, auth_base.validate_success_response)

    @staticmethod
    @allure.step("Генерация токена через POST /Account/v1/GenerateToken")
    def post_token_authorized():
        """
        Метод для генерации токена пользователя через POST-запрос на эндпоинт /Account/v1/GenerateToken.

        Этот метод используется для получения токена пользователя, используя предоставленные имя пользователя и пароль.
        В процессе выполнения метода происходит несколько шагов:

        1. Создается экземпляр класса `AuthBase`, где задаются параметры авторизации (имя пользователя и пароль).
        2. Формируются данные для запроса и полный URL для генерации токена.
        3. Выполняется отправка POST-запроса на сервер с предоставленными данными.
        4. Выполняется валидация ответа сервера, проверяется успешность генерации токена.

        В случае успешного получения токена, результат валидации добавляется в отчет Allure и выводится в консоль,
        включая сгенерированный токен. Если запрос на генерацию токена не удался, тест завершится с ошибкой, и информация
        об этом также будет включена в отчет Allure.
        """
        auth_base = AuthBase(username="MakeyStar", password="23MakeyStar23!/")

        with allure.step("Формирование данных и отправка запроса"):
            data, url = auth_base.form_request_data(auth_base.get_generate_token_endpoint())
            response = auth_base.send_post_request(data, url)

        with allure.step("Валидация ответа"):
            auth_base.validate_response(response, auth_base.validate_token_response)