from src.clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from tools.assertions.base import assert_equal
import httpx

def assert_create_file_response(request: CreateFileRequestSchema,response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу
    :param request: API запрос на создание файла
    :param response: API ответ с данными файла
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")


def assert_file_is_accessible(url: str):
    """
    Проверяет, что файл доступен по-указанному URL.

    :param url: Ссылка на файл.
    :raises AssertionError: Если файл не доступен.
    """
    response = httpx.get(url)
    assert response.status_code == 200, f"Файл недоступен по URL: {url}"