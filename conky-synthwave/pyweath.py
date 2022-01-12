#!/usr/bin/env python
# encoding: utf-8

import json
import datetime
try:
	from urllib.request import urlopen
except ImportError:
	from urllib import urlopen, urlencode

APPID = "your_appid"
CITY = "your_city"
API_URL = "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "&appid=" + APPID + "&units=metric"

def main():
    jsonResponse = urlopen(API_URL).read()
    pythonResponse = json.loads(jsonResponse)

    print('├ Temperature:',pythonResponse['main']['temp'],'°C')
    print('├ Min        :',pythonResponse['main']['temp_min'],'°C')
    print('├ Max        :',pythonResponse['main']['temp_max'],'°C')
    print('├ Feels Like :',pythonResponse['main']['feels_like'], '°C')
    print('├ Weather    :',pythonResponse['weather'][0]['main'])
    print('├ Description:',pythonResponse['weather'][0]['description'])
    print('├ Wind Speed :',pythonResponse['wind']['speed'], 'm/s')
    print('├ Humidity   :',pythonResponse['main']['humidity'], '%')
    print('├ Sunrise    :',datetime.datetime.fromtimestamp(pythonResponse['sys']['sunrise']).strftime('%H:%M:%S'))
    print('├ Sunset     :',datetime.datetime.fromtimestamp(pythonResponse['sys']['sunset']).strftime('%H:%M:%S'))

if __name__ == "__main__":
	main()
