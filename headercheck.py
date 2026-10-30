import requests

url = "https://example.com"  # Replace with the target URL
try:
    response = requests.get(url, timeout=10)
    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type", "Отсутствует"))
except requests.exceptions.RequestException as error:
    print("Произошла ошибка при выполнении запроса:", error)