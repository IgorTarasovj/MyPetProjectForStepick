import pytest

from src.fixtures.models.file_fixture import FileFixture
from src.clients.files.files_client import get_files_client, FilesClient
from src.clients.files.files_schema import CreateFileRequestSchema
from src.fixtures.models.user_fixture import UserFixture



@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    """
    Фикстура создает экземпляр FilesClient.
    :param Фикстура пользователя (UserFixture)
    :return: экземпляр FilesClient.
    """
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    """
    Фикстура создает тестовый файл через API и возвращает агрегированные данные
    :param files_client: Клиент для работы с API файлов (/api/v1/courses)
    :return: FileFixture с данными запроса и ответа
    """
    request = CreateFileRequestSchema(upload_file="./tests/testdata/files/image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)