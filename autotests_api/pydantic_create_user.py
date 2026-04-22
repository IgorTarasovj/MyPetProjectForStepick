import uuid

from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError

class UserShema (BaseModel):
    id: str = Field(default_factory=lambda : str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestShema(BaseModel):
    email: EmailStr
    password: str = Field(alias="password")
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseShema(BaseModel):
    user: UserShema