import pytest

from src.fixtures.models.user_fixture import UserFixture
from src.clients.users.private_users_client import get_private_users_client, PrivateUsersClient
from src.clients.users.public_users_client import get_public_users_client, PublicUsersClient
from src.clients.users.users_schema import CreateUserRequestSchema




@pytest.fixture
def public_users_client() -> PublicUsersClient:
    """
    Фикстура создает экземпляр PublicUsersClient
    :return: экземпляр PublicUsersClient.
    """
    return get_public_users_client()


@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    """
    Фикстура создает экземпляр PrivateUsersClient.
    :param результат фикстуры function_user(экземпляр UserFixture)
    :return: экземпляр PrivateUsersClient.
    """
    return get_private_users_client(function_user.authentication_user)


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    """
    Фикстура создает экземпляр UserFixture
    :param экземпляр PublicUsersClient(Клиент для работы с /api/v1/users)
    :return: экземпляр UserFixture(request: CreateUserRequestSchema, response: CreateUserResponseSchema)
    """
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)