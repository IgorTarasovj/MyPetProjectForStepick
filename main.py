from pydantic import BaseModel

from tools.assertions.base import assert_model, assert_model_match

class First(BaseModel):
    name: str | None = None
    id: str | None = None
    email: str | None = None

class Second(BaseModel):
    name: str | None = None
    id: str | None = None
    kal: str | None = None

first = First(name="first", id="1", email="asdasd")
second = Second(name="first", id="1")

assert_model_match(first, second)