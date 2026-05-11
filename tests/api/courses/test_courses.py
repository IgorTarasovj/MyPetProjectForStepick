from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema
from fixtures.models.course_fixture import CourseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response
from tools.assertions.schema import validate_json_schema

@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        request = UpdateCourseRequestSchema()

        response = courses_client.update_course_api(function_course.response.course.id, request)
        response_date = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_date)

        validate_json_schema(response.json(), response_date.model_json_schema())
