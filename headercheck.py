import requests

url = input("Enter the target URL: ")  
try:
    response = requests.get(url, timeout=10)
  
    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type", "Not Found"))
    headers_to_check = [
        "X-Content-Type-Options",
        "Content-Security-Policy",
        "Strict-Transport-Security",
    ]
    for header in headers_to_check:
        value = response.headers.get(header)
        if value is None:
            print("[Missing]", header)
        else:
            print("[Present]", header + ":", value)

except requests.exceptions.RequestException as error:
    print("Error occurred while fetching the URL:", error)
    