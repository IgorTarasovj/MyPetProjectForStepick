import pytest

from src.clients.exercises.exercises_client import ExercisesClient, get_exercise_client
from src.clients.exercises.exercises_schema import CreateExerciseRequestSchema
from src.fixtures.models.course_fixture import CourseFixture
from src.fixtures.models.exercise_fixture import ExerciseFixture
from src.fixtures.models.user_fixture import UserFixture


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
                      course_fixture: CourseFixture,
                      ) -> ExerciseFixture:
    """
    Фикстура создает задание через API и возвращает данные запроса и ответа
    :param exercise_client: Клиент для работы с API заданий(/api/v1/exercises)
    :param course_fixture: Фикстура добавления курса через API
    :return: ExerciseFixture с данными запроса и ответа
    """
    request = CreateExerciseRequestSchema(courseId=course_fixture.response.course.id)
    response = exercise_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
