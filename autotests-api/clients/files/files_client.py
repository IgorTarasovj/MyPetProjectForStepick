from typing import TypedDict

from httpx import Response

from ..api_client import APIClient

class CreateFileRequestDict(TypedDict):
    filename: str
    directory: str
    upload_file: str

class FilesClient(APIClient):

    def get_file_api(self, file_id: str) -> Response:
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request['upload_file'], 'rb')}
        )

    def delete_file_api(self, file_id: str) -> Response:
        return self.delete(f"/api/v1/files/{file_id}")