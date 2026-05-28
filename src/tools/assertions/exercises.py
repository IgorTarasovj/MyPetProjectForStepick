from clients.exercises.exercises_schema import PartialExerciseShema
from tools.assertions.base import assert_model


def assert_create_exercise_response(request: PartialExerciseShema, response: PartialExerciseShema):
    """
    Проверяет, что ответ на создание курса соответствует данным из запроса.

    :param request: Post запрос на создание задания
    :param response: Post ответ на создание задания
    :raises: AssertionError: Если данные не совпали
    """
    assert_model(request, response)

