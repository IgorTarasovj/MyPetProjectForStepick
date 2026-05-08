from pydantic import BaseModel, EmailStr

from src.clients.private_http_builder import AuthenticationUserSchema
from src.clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    """
    Описание структуры для агрегирования ответа API при создании пользователя(api/v1/users)
    Атрибуты:
        request (CreateUserRequestSchema): Структура запроса на создание пользователя(api/v1/users)
        response (CreateUserResponseSchema): Структура ответа на создание пользователя(api/v1/users)
    """
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)
