from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, PartialCourseSchema, GetCoursesResponseSchema, GetCoursesQuerySchema
from fixtures.models.course_fixture import CourseFixture
from fixtures.models.user_fixture import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response
from tools.assertions.schema import validate_json_schema

@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_update_course(self,
                           courses_client: CoursesClient,
                           function_course: CourseFixture):
        request = UpdateCourseRequestSchema()

        response = courses_client.update_course_api(function_course.response.course.id, request)
        response_date = UpdateCourseResponseSchema.model_validate_json(response.text)

        request_partial = PartialCourseSchema(
            title = request.title,
            maxScore=request.max_score,
            minScore=request.min_score,
            description=request.description,
            estimatedTime=request.estimated_time
        )

        response_partial = PartialCourseSchema(
            title = response_date.course.title,
            maxScore=response_date.course.max_score,
            minScore=response_date.course.min_score,
            description=response_date.course.description,
            estimatedTime=response_date.course.estimated_time

        )

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request_partial, response_partial)

        validate_json_schema(response.json(), response_date.model_json_schema())

    def test_get_courses(
            self,
            courses_client: CoursesClient,
            function_user: UserFixture,
            function_course: CourseFixture
    ):
        query = GetCoursesQuerySchema(userId=function_user.response.user.id)
        response = courses_client.get_courses_api(query)

        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])

        validate_json_schema(response.json(), response_data.model_json_schema())
