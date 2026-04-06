from typing import TypedDict

from httpx import Response

from ..api_client import APIClient

class GetCourseQueryDict(TypedDict):
    userId: int

class CreateCourseRequestDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCourseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(APIClient):
    def get_courses_api(self, query: GetCourseQueryDict) -> Response:
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        return self.delete(f"/api/v1/courses/{course_id}")