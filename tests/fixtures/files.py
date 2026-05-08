import pytest

from src.fixtures.models.file_fixture import FileFixture
from src.clients.files.files_client import get_files_client, FilesClient
from src.clients.files.files_schema import CreateFileRequestSchema
from src.fixtures.models.user_fixture import UserFixture



@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    """
    Фикстура создает экземпляр FilesClient.
    :param результат фикстуры function_user(экземпляр UserFixture)
    :return: экземпляр FilesClient.
    """
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    """
    Фикстура создает тестовый файл
    :param files_client: экземпляр FilesClient(клиент для работы с файлами)
    :return: экземпляр FileFixture(request: CreateFileRequestSchema, response: CreateFileResponseSchema)
    """
    request = CreateFileRequestSchema(upload_file="./tests/testdata/files/image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)