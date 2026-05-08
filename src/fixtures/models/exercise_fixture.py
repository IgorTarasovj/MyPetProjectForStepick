from pydantic import BaseModel

from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema


class ExerciseFixture(BaseModel):
    """
    Описание структуры для агрегации возвращаемых данных при работе с api/v1/exercises
    Attributes:
        request (CreateCourseRequestSchema): Структура запроса на создание курса(api/v1/exercises)
        response (CreateCourseResponseSchema): Структура ответа на создание курса(api/v1/exercises)
    """
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema