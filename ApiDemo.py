import requests

def main():
    url = "http://localhost:8000/users/6"
    payload = {
        "name": "Raj",
        "city": "Bengaluru",
        "email": "raj@example.com",
        "age": 20,
    }
    headers = {"Content-Type": "application/json"}

    
    response = requests.put(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("Response:", data)


if __name__ == "__main__":
    main()
