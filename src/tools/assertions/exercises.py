from clients.exercises.exercises_schema import PartialExerciseShema, ExerciseSchema, GetExerciseResponseSchema, \
    CreateExerciseResponseSchema
from tools.assertions.base import assert_model, assert_length


def assert_create_exercise_response(request: PartialExerciseShema, response: PartialExerciseShema):
    """
    Проверяет, что ответ на создание курса соответствует данным из запроса.

    :param request: Post запрос на создание задания
    :param response: Post ответ на создание задания
    :raises: AssertionError: Если данные не совпали
    """
    assert_model(request, response)

def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.
    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises: AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_model(actual, expected)

def assert_get_exercise_response(get_exercises_response, create_exercise_response):
    """
    Проверяет, что данные задания, полученным в GET-запросе, соответствуют созданному в POST-запросе
    :param get_exercises_response: Данные задания из GET api/v1/exercise{exercise_id}
    :param create_exercise_response: Ответ POST запроса api/v1/exercises
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    assert_model(get_exercises_response, create_exercise_response)

def assert_get_exercises_response(get_exercises_response: GetExerciseResponseSchema,
                                 create_exercise_response: list[CreateExerciseResponseSchema]):

    """
    Проверяет, что ответ на получение списка заданий соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка заданий.
    :param create_exercise_response: Список API ответов при создании заданий.
    :raises: AssertionError: Если данные заданий не совпадают.
    """

    assert_length(get_exercises_response.exercises, create_exercise_response, "courses")

    for index, create_exercise_response in enumerate(create_exercise_response):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)