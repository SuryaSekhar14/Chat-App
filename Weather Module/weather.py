#python script to find the weather of a city using Openweathermap API.

import requests
import json

api_key = "1d294d3de5d382efdd53570850ba10a9" #api key for Openweathermap API

base_url = "http://api.openweathermap.org/data/2.5/weather?" #base url for the api

city_name = input("Enter City Name:")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name #complete url for the response

#print(complete_url)

response = requests.get(complete_url)

#print(response.text)

x = response.json()

if x["cod"] != "404":
 
    # store the value of "main"
    # key in variable y
    y = x["main"]
 
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
 
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
 
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
 
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
 
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]
 
    # print following values
    print(" Temperature (in celsius unit) = " +
                    str(int(current_temperature - 273.15)) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description))
 
else:
    print(" City Not Found ")