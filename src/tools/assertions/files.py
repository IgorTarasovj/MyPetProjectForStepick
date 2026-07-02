import allure

from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, GetFileResponseSchema
from tools.assertions.base import assert_equal, assert_model
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
import httpx
from config import settings
from tools.logger import get_logger
from tools.assertions.expected_errors import empty_filename_error, empty_directory_error, incorrect_file_id_error

logger = get_logger("FILES_ASSERTIONS")

@allure.step("Check create file response")
def assert_create_file_response(request: CreateFileRequestSchema,response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу
    :param request: API запрос на создание файла
    :param response: API ответ с данными файла
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    logger.info("Check create file response")
    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")

    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")

@allure.step("Check file is accessible")
def assert_file_is_accessible(url: str):
    """
    Проверяет, что файл доступен по-указанному URL.

    :param url: Ссылка на файл.
    :raises AssertionError: Если файл не доступен.
    """
    logger.info("Check file is accessible")
    response = httpx.get(url)
    assert response.status_code == 200, f"Файл недоступен по URL: {url}"

@allure.step("Check file")
def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет, что фактические данные файла соответствуют ожидаемым
    :param actual: Фактические данные файла
    :param expected: Ожидаемые данные файла
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    logger.info("Check file")
    assert_model(actual, expected)

@allure.step("Check get file response")
def assert_get_file_response(get_file_response: GetFileResponseSchema, create_file_response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на получение файла соответствует ответу на его создание

    :param get_file_response: Ответ GET-запроса api/v1/file{file_id}
    :param create_file_response: Ответ POST-запроса api/v1/files
    :raises AssertionError: Если данные файла не совпадают
    """
    logger.info("Check get file response")
    assert_file(get_file_response.file, create_file_response.file)

@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check create file with empty filename response")
    expected = empty_filename_error()
    assert_validation_error_response(actual, expected)

@allure.step("Check create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check create file with empty directory response")
    expected = empty_directory_error()
    assert_validation_error_response(actual, expected)

@allure.step("Check file not found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    logger.info("Check file not found response")
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check get file with incorrect file id response")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на GET-запрос api/v1/files{file_id} c некорректным file_id соответствует ожидаемой валидационной ошибке
    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check get file with incorrect file id response")
    expected = incorrect_file_id_error()
    assert_validation_error_response(expected, actual)