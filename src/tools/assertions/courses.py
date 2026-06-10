from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    PartialCourseSchema, GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.assertions.base import assert_equal, assert_model, assert_model_match, assert_length, assert_diff_model
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


def assert_update_course_response(
        request: UpdateCourseRequestSchema, response: CourseSchema
):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_diff_model(request, response)


def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что фактические данные курса соответствуют ожидаемым.

    :param actual: Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_model(
        actual,
        expected,
        exclude={"preview_file", "created_by_user"}
    )

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)


def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

    :param get_courses_response: Ответ API при запросе списка курсов.
    :param create_course_responses: Список API ответов при создании курсов.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    assert_length(get_courses_response.courses, create_course_responses, "courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_response.course)


def assert_create_course_response(request: CreateCourseRequestSchema,
                                  user_request: UserSchema,
                                  file_request: FileSchema,
                                  response: CourseSchema):
    """
    Проверяет, что ответ на создание курса соответствует данным из запроса на создание

    :param request: Post запрос на создание курса
    :param user_request: UserSchema соответствующая createdByUserId в запросе
    :param file_request: FileSchema соответствующая previewFileId в запросе
    :param response: Post ответ на создание курса
    :raises AssertionError: Если данные не совпадают.
    """
    assert_diff_model(request,
                 response,
                 exclude={"preview_file", "created_by_user"})

    assert_file(file_request, response.preview_file)
    assert_user(user_request, response.created_by_user)