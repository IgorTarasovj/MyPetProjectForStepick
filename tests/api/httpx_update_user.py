import httpx
from src.tools.fakers import fake

create_user_request = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_request)
create_user_response_data = create_user_response.json()
user_id = create_user_response_data['user']['id']

print(create_user_response.json())
print(create_user_response.status_code)

authentication_request = {
    "email": create_user_request['email'],
    "password": create_user_request['password']
}

authentication_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=authentication_request)
accessToken = authentication_response.json()['token']['accessToken']

print(authentication_response.json())
print(authentication_response.status_code)

update_user_response_body = {
    "lastName": "changelastname",
    "firstName": "changefirstname",
    "middleName": "changemiddlename"
}

headers = {
    "Authorization": f"Bearer {accessToken}"
}

update_user_response = httpx.patch(f'http://localhost:8000/api/v1/users/{user_id}', json=update_user_response_body, headers=headers)
update_user_response_data = update_user_response.json()

print(update_user_response.json())
print(update_user_response.status_code)