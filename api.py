from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_URL="https://api.openweathermap.org/data/2.5/weather?"
CITY="London"
API_KEY=os.getenv("API_KEY")

params={"q":CITY,"appid":API_KEY}
response=requests.get(API_URL,params=params)

if response.status_code==200:
    weather_data=response.json()
    print("Fetched data:",json.dumps(weather_data,indent=4))
else:
    print("Failed to get data.Status code: ",response.status_code)


