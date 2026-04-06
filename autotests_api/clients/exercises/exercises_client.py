from typing import TypedDict

from httpx import Response

from ..api_client import APIClient
from ..private_http_builder import get_private_http_client, AuthenticationUserDict

class Exercise(TypedDict):
    """
    Описание структуры задания
    """
    id : str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesListDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий
    """
    courseId: str

class CreateExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа создания задания
    """
    exercise: Exercise


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercise_api(self, query: GetExercisesListDict) -> Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.get("/api/v1/exercises", params=query)

    def get_exercises_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с id, title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self,exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExercisesResponseDict:
        """
        Метод возвращает ответ от post_exercise_api в формате json
        :param request:Словарь с id, title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return:Ответ от сервера в формате json
        """
        response= self.create_exercise_api(request)
        return response.json()

def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExerciseClient с уже настроенным HTTP-клиентом.
    :param user:
    :return:
    """
    return ExercisesClient(client=get_private_http_client(user))