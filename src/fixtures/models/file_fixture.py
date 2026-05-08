from pydantic import BaseModel
from src.clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema

class FileFixture(BaseModel):
    """
    Описание структуры для агрегации возвращаемых данных при работе с файлами
    """
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema