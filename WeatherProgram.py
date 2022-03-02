import json
from json import JSONDecodeError
from multiprocessing.sharedctypes import Value
from pprint import pprint
from sqlite3 import paramstyle
import requests
from geopy.geocoders import Nominatim
from pprint import pprint
from time import sleep

loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("Adres")
Latitude = getLoc.latitude
Longitude = getLoc.longitude

params = {
    "current_weather" : "true",
    "latitude" : Latitude,
    "longitude" : Longitude
}
weather = requests.get("https://api.open-meteo.com/v1/forecast/", params)

try:
    weatherInfo = weather.json()
except JSONDecodeError:
    print("Niepoprawny format")
else:
    answer = ''
    while answer != 'tak':
        current_weather = weatherInfo['current_weather']
        temperature = current_weather['temperature']
        windspeed = current_weather['windspeed']
        winddirection = current_weather['winddirection']
        time = current_weather['time']
        print('''Pogoda na dzień %s w twojej lokalizacji.
Temperatura wynosi %d°C
Siła wiatru to %d km\h
        ''' %(time, temperature, windspeed))
        sleep(1)
        answer = input("Czy chcesz zamknąć program? [tak/nie]")