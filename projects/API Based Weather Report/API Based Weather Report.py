import requests
import os
from datetime import datetime

location = input("\nEnter the city name   : ")

api_key = "Enter your api key here"
complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data

try:
    temp_city = (api_data["main"]["temp"]) - 273.15
    weather_desc = api_data["weather"][0]["description"]
    hmdt = api_data["main"]["humidity"]
    wind_spd = api_data["wind"]["speed"]
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    with open("wetherinfo.txt", "w+") as f:
        f.write("-------------------------------------------------------------\n")
        f.write(f"Weather Stats for - {location.upper()}  || {date_time}\n")
        f.write("-------------------------------------------------------------\n")

        f.write("\tCurrent temperature is : {:.2f} °C\n".format(temp_city))
        f.write("\tCurrent weather desc   : " + weather_desc + "\n")
        f.write(f"\tCurrent Humidity       : {hmdt} %\n")
        f.write(f"\tCurrent wind speed     : {wind_spd} km/h \n")
    print("Current temperature is: {:.2f} °C".format(temp_city))
    print(f"Current weather desc  : {weather_desc}")
    print("Current Humidity      :", hmdt, "%")
    print("Current wind speed    :", wind_spd, "kmph")

except KeyError as KE:
    print("Enter a valid city")
