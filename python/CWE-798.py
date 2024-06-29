import requests

def make_request():
    # Жестко заданные учетные данные (уязвимость CWE-798)
    username = "admin"
    password = "password123"

    # URL для отправки запроса
    url = "https://example.com/api/data"

    # Выполнение запроса с использованием жестко заданных учетных данных
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        print("Request successful!")
        print("Data:", response.json())
    else:
        print("Request failed with status code:", response.status_code)

if __name__ == "__main__":
    make_request()
