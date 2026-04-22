import uuid

from pydantic import BaseModel, Field, ConfigDict

class ExerciseSchema(BaseModel):
    """
    Описание структуры задания
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str =Field(default=str(uuid.uuid4()))
    title: str
    course_id: str = Field(alias="courseId", default=str(uuid.uuid4()))
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExerciseSchema(BaseModel):

    """
    Описание структуры запроса на получение списка заданий
    """
    courseId: str

class CreateExerciseResponseSchema(BaseModel):

    """
    Описание структуры ответа создания задания
    """
    exercise: ExerciseSchema

class CreateExerciseRequestSchema(BaseModel):

    """
    Описание структуры запроса на создание задания
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId", default=str(uuid.uuid4()))
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")