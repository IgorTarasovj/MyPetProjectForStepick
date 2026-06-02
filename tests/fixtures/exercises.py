import pytest

from clients.exercises.exercises_client import ExercisesClient, get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from fixtures.models.course_fixture import CourseFixture
from fixtures.models.exercise_fixture import ExerciseFixture
from fixtures.models.user_fixture import UserFixture


@pytest.fixture(scope="function")
def exercise_client(function_user: UserFixture)-> ExercisesClient:
    """
    Фикстура создает экземпляр ExercisesClient
    :param function_user: Фикстура создания пользователя
    :return: экземпляр ExercisesClient
    """
    return get_exercise_client(function_user.authentication_user)

@pytest.fixture(scope="function")
def function_exercise(exercise_client: ExercisesClient,
                      function_course: CourseFixture,
                      ) -> ExerciseFixture:
    """
    Фикстура создает задание через API и возвращает данные запроса и ответа
    :param exercise_client: Клиент для работы с API заданий(/api/v1/exercises)
    :param function_course: Фикстура добавления курса через API
    :return: ExerciseFixture с данными запроса и ответа
    """
    request = CreateExerciseRequestSchema(courseId=function_course.response.course.id)
    response = exercise_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
