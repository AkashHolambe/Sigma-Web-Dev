import requests

api_key = "your_api_key_here"
url = f"http://api.openweathermap.org/data/2.5/weather?q=CityName&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    # Process the data from the API response
    data = response.json()
    print(data)
else:
    # Handle the error
    print(f"Error: {response.status_code}, {response.json()}")
