import httpx
from pprint import pprint


login_payload = {
    "email": "user@example.com",
    "password": "1"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response.status_code)
pprint(login_response.json())

refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

print(refresh_payload)

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print(refresh_response.status_code)
pprint(refresh_response_data)