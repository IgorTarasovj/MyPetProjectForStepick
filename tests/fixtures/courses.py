import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.models.file_fixture import FileFixture
from fixtures.models.user_fixture import UserFixture
from fixtures.models.course_fixture import CourseFixture


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    """
    Фикстура создает экземпляр CoursesClient.
    :param function_user: Фикстура создания пользователя
    :return: экземпляр CoursesClient
    """
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> CourseFixture:
    """
    Фикстура создает тестовый курс через API и возвращает агрегированные данные
    :param courses_client: Клиент для работы с API курсов (/api/v1/courses)
    :param function_user: Фикстура добавления пользователя (UserFixture) через API
    :param function_file: Фикстура добавления файла (FileFixture) через API
    :return: CourseFixture с данными запроса и ответа
    """
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)