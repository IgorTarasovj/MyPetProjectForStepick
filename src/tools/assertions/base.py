from typing import Any, Sized
from pydantic import BaseModel


def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )

def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param actual:Название проверяемого значения.
    :param expected:Фактическое значение.
    :param name: Название проверяемого поля
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}'
    )


def assert_is_true(actual: Any,  name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )

def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    assert len(actual) == len(expected), (
        f'Incorrect object length: "{name}". '
        f'Expected length: {len(expected)}. '
        f'Actual length: {len(actual)}'
    )

def assert_model(
        actual: BaseModel,
        expected: BaseModel,
        exclude: set[str] | None = None
):
    """
    Сравнивает две Pydantic модели по каждому полю.

    :param actual: Фактическая Pydantic модель.
    :param expected: Ожидаемая Pydantic модель.
    :param exclude: Поля, которые необходимо исключить из сравнения.
    :raises AssertionError: Если значения полей не совпадают.
    """
    exclude = exclude or set()

    expected_data = expected.model_dump(exclude=exclude)

    for field, expected_value in expected_data.items():
        actual_value = getattr(actual, field)
        assert_equal(actual_value, expected_value, field)


def assert_model_match(actual: BaseModel, expected: BaseModel):
    """
    Сравнивает две Pydantic модели по каждому полю, допускает пустые значения
    :param actual: Фактическая Pydantic модель
    :param expected: Ожидаемая Pydantic модель
    :raises AssertionError: Если фактическое значение какого либо из полей не равно ожидаемому.
    """
    expected_data = expected.model_dump(exclude_none=True)

    for field, value in expected_data.items():
        actual_value = getattr(actual, field)
        expected_value = getattr(expected, field)
        assert_equal(actual_value, expected_value, field)
