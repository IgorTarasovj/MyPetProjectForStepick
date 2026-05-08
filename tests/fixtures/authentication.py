import pytest

from src.clients.authentication.authentication_client import AuthenticationClient, get_authentication_client


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    """
    Фикстура создает экземпляр AuthenticationClient
    :return: экземпляр AuthenticationClient.
    """
    return get_authentication_client()