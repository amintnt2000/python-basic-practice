import requests

try:
    response = requests.post(
        "http://127.0.0.1:5000/users",
        json={"name": "max", "email": "max@gmail.com"},
        timeout=5
    )
    print(response.status_code)
    print(response.json())
except requests.exceptions.ConnectionError as e:
    print("Connection Error:", e)
except requests.exceptions.Timeout:
    print("Request timed out")
