import requests

url = "https://example.com"  # Replace with the target URL
try:
    response = requests.get(url, timeout=10)
    value = response.headers.get("X-Content-Type-Options")
    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type", "Отсутствует"))
   
    if value is None:
       print("[Missing] X-Content-Type-Options")
    else:
       print("[Present] X-Content-Type-Options:", value)

except requests.exceptions.RequestException as error:
    print("Произошла ошибка при выполнении запроса:", error)
    