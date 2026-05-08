from pydantic import BaseModel

from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema


class CourseFixture(BaseModel):
    """
    Описание структуры для агрегации возвращаемых данных при работе с api/v1/courses
        request (CreateCourseRequestSchema): Структура запроса на создание курса(api/v1/courses)
        response (CreateCourseResponseSchema): Структура ответа на создание курса(api/v1/courses)
    """
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema