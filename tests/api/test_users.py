from http import HTTPStatus

import pytest

from src.clients.users.private_users_client import PrivateUsersClient
from src.clients.users.public_users_client import PublicUsersClient
from src.clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tests.api.conftest import UserFixture
from tools.assertions.schema import  validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):
    """
    Проверка создания пользователя(POST /api/v1/users)
    """
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())



@pytest.mark.regression
@pytest.mark.user
def test_get_user_me(function_user: UserFixture,
                     private_users_client: PrivateUsersClient):

    response = private_users_client.get_user_api(function_user.response.user.id)
    assert_status_code(response.status_code, HTTPStatus.OK)

    response_data = GetUserResponseSchema.model_validate_json(response.text)
    assert_get_user_response(function_user.response.user, response_data.user)

    validate_json_schema(response.json(), response_data.model_json_schema())
