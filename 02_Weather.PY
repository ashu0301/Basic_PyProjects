from calendar import day_abbr
from urllib import response
import requests

API_KEY = "a2e72e2fc0c918f4d061828211148849"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter aa city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(f"Weather in {city}:",weather)
    temperature = round(data['main']['temp'] - 273.15,2)
    print(f"Temperature in {city}: {temperature} Cel")
else:
    print("An error occured")
