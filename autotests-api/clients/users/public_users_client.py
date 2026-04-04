from typing import TypedDict

from httpx import Response

from ..api_client import APIClient

class CreateUserApiDict(TypedDict):
    email : str
    password : str
    first_name : str
    last_name : str
    middle_name : str

class PublicUsersClient(APIClient):

    def create_user_api(self, request: CreateUserApiDict ) -> Response:
        return self.post("/api/v1/users", json=request)
