import requests
from requests.auth import HTTPBasicAuth

print(requests.get("http://localhost:5000/basic-protected").text)
print(requests.get("http://localhost:5000/jwt-protected").text)

access_token = requests.post(
    "http://localhost:5000/login",
    json = {"username": "Arnaud", "password": "hello"},
    headers = { "Content-Type":  "application/json" }
).json()["access_token"]

print(f"JWT: {access_token[0:80]}...")

print(requests.get("http://localhost:5000/basic-protected", auth=HTTPBasicAuth("Arnaud", "hello")).text)
print(requests.get("http://localhost:5000/jwt-protected", headers = { "Authorization": f"Bearer {access_token}" }).text)

print(requests.get("http://localhost:5000/admin-only", headers = { "Authorization": f"Bearer {access_token}" }).text)

print(requests.get("http://localhost:5000/admin-only", headers = { "Authorization": f"Bearer fdhsgfj" }).status_code)