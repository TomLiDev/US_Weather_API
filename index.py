import requests
import pandas as pd

URL = "https://api.weather.gov.points/33.997,-120.4833"

URL2 = "https://api.weather.gov/gridpoints/TOP/31,80/forecast"

response = requests.get(URL2)

response.json()
data = response.json()

print("full json", response.json())
print("\n \n Specific", response.json()["properties"])
print("\n \n Very specific", response.json()["properties"]['generatedAt'])

periods = response.json()['properties']['periods']

temp_dict = {}
for period in periods:
    temp_dict[period['startTime']] = period['temperature']

print("\n \n Temp dict", temp_dict)