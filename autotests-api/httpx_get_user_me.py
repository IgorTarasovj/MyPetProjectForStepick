import httpx
from pprint import pprint

authentication_login_body = {
    "email": "user@example.com",
    "password": "1"
}

authentication_login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=authentication_login_body)

print(authentication_login_response.status_code)
pprint(authentication_login_response.json())

access_token = authentication_login_response.json()["token"]["accessToken"]
headers = {'Authorization': f'Bearer {access_token}'}

users_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(users_me_response.status_code)
pprint(users_me_response.json())