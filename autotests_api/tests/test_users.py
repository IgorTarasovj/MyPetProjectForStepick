from http import HTTPStatus
from autotests_api.clients.users.public_users_client import get_public_users_client
from autotests_api.clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


def test_create_user():
    """
    Проверка создания пользователя(POST /api/v1/users)
    """
    public_users_client = get_public_users_client()

    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert response.status_code == HTTPStatus.OK, "Incorrect status code"
    assert response_data.user.email == request.email, "Incorrect email"
    assert response_data.user.last_name == request.last_name, "Incorrect last_name"
    assert response_data.user.first_name == request.first_name, "Incorrect first_name"
    assert response_data.user.middle_name == request.middle_name, "Incorrect middle_name"