from typing import TypedDict

from httpx import Response

from ..api_client import APIClient
from ..public_http_builder import get_public_http_client

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры создания пользователя
    """
    email : str
    password : str
    first_name : str
    last_name : str
    middle_name : str

class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict ) -> Response:
        """
        Метод отправляет запрос на создание пользователя
        :param request: Словарь с email, password, first_name, last_name, middle_name
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        """
        Метод возвращает ответ на запрос метода create_user_api в виде json
        :param request: Словарь с email, password, first_name, last_name, middle_name
        :return: Ответ от сервера в формате json
        """
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())