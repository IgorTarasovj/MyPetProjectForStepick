from http import HTTPStatus

import pytest

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    PartialExerciseShema, GetExerciseSchema, GetExerciseResponseSchema, ExerciseSchema, UpdateExerciseRequestSchema, \
    UpdateExerciseResponseSchema, GetExercisesResponseSchema
from fixtures.models.course_fixture import CourseFixture
from fixtures.models.exercise_fixture import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.exercises
class TestExercises:
    def test_create_exercise(self, exercise_client: ExercisesClient,
                             function_course: CourseFixture):


        request = CreateExerciseRequestSchema(courseId=function_course.response.course.id)

        response = exercise_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        partial_request = PartialExerciseShema(
            title=request.title,
            description=request.description,
            courseId=request.course_id,
            maxScore=request.max_score,
            minScore=request.min_score,
            orderIndex=request.order_index,
            estimatedTime=request.estimated_time
        )


        partial_response = PartialExerciseShema(
            title=response_data.exercise.title,
            description=response_data.exercise.description,
            courseId=response_data.exercise.course_id,
            maxScore=response_data.exercise.max_score,
            minScore=response_data.exercise.min_score,
            orderIndex=response_data.exercise.order_index,
            estimatedTime=response_data.exercise.estimated_time

        )

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(partial_request, partial_response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(self, exercise_client: ExercisesClient,
                          function_exercise: ExerciseFixture):

        response = exercise_client.get_exercises_api(function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(function_exercise.response.exercise, response_data.exercise)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(self, exercise_client: ExercisesClient,
                             function_exercise: ExerciseFixture):
        request = UpdateExerciseRequestSchema()

        response = exercise_client.update_exercise_api(function_exercise.response.exercise.id, request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        partial_request = PartialExerciseShema(
            title=request.title,
            description=request.description,
            maxScore=request.max_score,
            minScore=request.min_score,
            orderIndex=request.order_index,
            estimatedTime=request.estimated_time
        )

        partial_response = PartialExerciseShema(
            title=response_data.exercise.title,
            description=response_data.exercise.description,
            maxScore=response_data.exercise.max_score,
            minScore=response_data.exercise.min_score,
            orderIndex=response_data.exercise.order_index,
            estimatedTime=response_data.exercise.estimated_time
        )

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(partial_request, partial_response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_delete_exercise(self, exercise_client: ExercisesClient,
                             function_exercise: ExerciseFixture):

        delete_response = exercise_client.delete_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercise_client.get_exercises_api(function_exercise.response.exercise.id)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)

        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)
        assert_exercise_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    def test_get_exercises(self, exercise_client: ExercisesClient, function_exercise: ExerciseFixture):

        query = GetExerciseSchema(courseId=function_exercise.response.exercise.course_id)

        response = exercise_client.get_exercise_api(query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])

        validate_json_schema(response.json(), response_data.model_json_schema())
