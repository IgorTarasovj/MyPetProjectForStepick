from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, PartialUserSchema
from tools.assertions.base import assert_equal, assert_model, assert_model_match, assert_diff_model


def assert_create_user_response(request: CreateUserRequestSchema, response: UserSchema):
    """

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_diff_model(request, response)

def assert_user(actual : UserSchema, expected : UserSchema):
    """
    Проверяет, что данные пользователя соответствуют ожидаемым
    :param actual: Фактический пользователь
    :param expected: Ожидаемый пользователь
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    assert_model(actual, expected)

def assert_get_user_response(get_user_response, create_user_response):
    """
    Проверяет, что данные пользователя, полученным в GET-запросе, соответствуют созданному в POST-запросе
    :param get_user_response: Данные пользователя из GET api/v1/user{user_id}
    :param create_user_response: Ответ POST запроса api/v1/users
    :raises AssertionError: Если хотя бы одно поле не совпадает
    """
    return assert_model(get_user_response, create_user_response)