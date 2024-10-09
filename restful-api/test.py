import requests
from requests.auth import HTTPBasicAuth

users = {
    "user1": {"username": "user1", "password": "<hashed_password>", "role": "user"},
    "admin1": {"username": "admin1", "password": "<hashed_password>", "role": "admin"},
    "hello": {"username": "hello", "password": "<hashed_password>", "role": "admin"}
}

def send(endpoint: str, method = "GET", basic_auth = None, jwt_token = None):
    req = requests.request(
        method, f"http://localhost:5000/{endpoint}",
        auth = basic_auth,
        headers = { "Authorization": f"Bearer {jwt_token}" } if jwt_token else None
    )

    print(req.headers)

send("basic-protected")

# send(requests.get("http://localhost:5000/basic-protected").text)
# print(requests.get("http://localhost:5000/jwt-protected").text)

# access_token = requests.post(
#     "http://localhost:5000/login",
#     json = {"username": "Arnaud", "password": "hello"},
#     headers = { "Content-Type":  "application/json" }
# ).json()["access_token"]

# print(f"JWT: {access_token[0:80]}...")

# print(requests.get("http://localhost:5000/basic-protected", auth=HTTPBasicAuth("Arnaud", "hello")).text)
# print(requests.get("http://localhost:5000/jwt-protected", headers = { "Authorization": f"Bearer {access_token}" }).text)

# print(requests.get("http://localhost:5000/admin-only", headers = { "Authorization": f"Bearer {access_token}" }).text)

# print(requests.get("http://localhost:5000/admin-only", headers = { "Authorization": f"Bearer fdhsgfj" }).status_code)