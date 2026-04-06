from typing import TypedDict

from httpx import Response

from ..api_client import APIClient

class GetExercisesListDict(TypedDict):
    courseId: str

class CreateExercisesDict(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExercisesDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class ExercisesClient(APIClient):
    def get_exercises(self, query: GetExercisesListDict) -> Response:
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def post_exercise_api(self, request: CreateExercisesDict) -> Response:
        return self.post("/api/v1/exercises", json=request)

    def patch_exercise_api(self, request: UpdateExercisesDict) -> Response:
        return self.patch("/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        return self.delete(f"/api/v1/exercises/{exercise_id}")