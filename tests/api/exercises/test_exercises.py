from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    PartialExerciseShema, GetExerciseSchema, GetExerciseResponseSchema, ExerciseSchema
from fixtures.models.course_fixture import CourseFixture
from fixtures.models.exercise_fixture import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response
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