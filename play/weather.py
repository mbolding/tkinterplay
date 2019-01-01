#!/usr/bin/env python
# quickWeather.py - Prints the weather for a location from the command line.
# this is a pain in the ass just to check the weather

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()
location = " ".join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API.
# Download the JSON data from OpenWeatherMap.org's API.
# bbf1fdff6cd1d5b0ae3f91ded1608bc7
url = (
    "http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=fedbb265a408cd3faa1e8e291dffa3ca"
    % (location)
)
response = requests.get(url)
response.raise_for_status()


# TODO: Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.
w = weatherData["list"]
print("Current weather in %s:" % (location))
print(w[0]["weather"][0]["main"], "-", w[0]["weather"][0]["description"])
print()
print("Tomorrow:")
print(w[1]["weather"][0]["main"], "-", w[1]["weather"][0]["description"])
print()
print("Day after tomorrow:")
print(w[2]["weather"][0]["main"], "-", w[2]["weather"][0]["description"])
