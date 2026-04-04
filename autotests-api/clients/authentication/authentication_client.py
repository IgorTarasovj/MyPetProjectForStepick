from typing import TypedDict

from httpx import Response

from ..api_client import APIClient

class LoginRequestDict(TypedDict):
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    refresh_token: str

class AuthenticationClient(APIClient):

    def login_api(self, request: LoginRequestDict) ->Response:
        return  self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)