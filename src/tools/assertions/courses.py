from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema
from tools.assertions.base import assert_equal


def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema
):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """

    request_data = request.model_dump(exclude_none=True)

    for field, expected_value in request_data.items():
        actual_value = getattr(response.course, field)
        assert_equal(actual_value, expected_value, field)

    assert request_data, "Update request is empty — nothing to validate"