from pydantic import BaseModel
from src.clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema

class FileFixture(BaseModel):
    """
    Описание структуры для агрегации возвращаемых данных при работе с api/v1/files
    Attributes:
        request (CreateFileRequestSchema): Структура запроса на создание файла(api/v1/files)
        response (CreateFileResponseSchema): Структура ответа на создание файла(api/v1/files)
    """
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema