from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema


def empty_filename_error() -> ValidationErrorResponseSchema:
    return ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="missing",
                input=None,
                message="Field required",
                location=["body", "filename"]
            )
        ]
    )

def empty_directory_error() -> ValidationErrorResponseSchema:
    return ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="missing",
                input=None,
                message="Field required",
                location=["body", "directory"]
            )
        ]
    )

def incorrect_file_id_error() -> ValidationErrorResponseSchema:
    return ValidationErrorResponseSchema(
        details = [
            ValidationErrorSchema(
                type = "uuid_parsing",
                location=["path", "file_id"],
                message = "Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input = "incorrect-file-id",
                context = {"error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"}
            )
        ]
    )

def empty_exercise_error() -> InternalErrorResponseSchema:
    return InternalErrorResponseSchema(
        details="Exercise not found"
    )