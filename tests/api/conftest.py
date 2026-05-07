import pytest
from pydantic import BaseModel, EmailStr

from src.clients.users.private_users_client import get_private_users_client
from src.clients.users.private_users_client import PrivateUsersClient
from src.clients.private_http_builder import AuthenticationUserSchema
from src.clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from src.clients.users.public_users_client import get_public_users_client, PublicUsersClient
from src.clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

class UserFixture(BaseModel):
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
        return AuthenticationUserSchema(email = self.request.email, password = self.request.password)

@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)

@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(user=function_user.authentication_user)


