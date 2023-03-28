import random
import requests
import json
import time
import math
import chardet
import schedule
import os
from twilio.rest import Client


class Weather:
    def __init__(self,weather):

        print(weather)

        self.wind = weather.get("wind").get("speed")
        self.currentWeather = weather['weather'][0]['main']
        self.weatherDescription = weather['weather'][0]['description'].capitalize()
        self.temp = weather.get("main").get("temp")
        self.feels_like = weather.get("main").get("feels_like")
        self.temp_min = weather.get("main").get("temp_min")
        self.temp_max = weather.get("main").get("temp_max")
        self.pressure = round(weather.get("main").get("pressure")*0.02952998330101,2)
        self.humidity = weather.get("main").get("humidity")
        

    def __str__(self) -> str:
        return "Curent Weather for " + location +" is "+self.currentWeather+" with "+self.weatherDescription+"\nCurrent Temp is "+str(int(self.temp))+"F, It feels like "+ str(int(self.feels_like))+"F, today's temps will range from "+str(int(self.temp_min)) +"F to "+ str(int(self.temp_max))+"F, current pressure is "+ str(self.pressure)+ "in, and current humidity is "+str(self.humidity)+"%\n"+"Current wind speed is " + str(self.wind) +"mph\nHave a Nice Day!"
        


key = "f2d119dcb84fc5b14008222e22c425b3"
location = 'Normal'
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+key+"&units=imperial")
weather = json.loads(response.text)
while weather.get("cod") == '404':
    print("city not found")
    location = input("Enter the name of a City: ")
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+key+"&units=imperial")
    weather = json.loads(response.text)
else:
    weather1 = Weather(weather)
    print(weather1)      







account_sid = "AC589765d5bdd03122235bb650f3363311"
auth_token ="5a6d2dc242fc8517e91255b8dd18556f"

client = Client(account_sid,auth_token)

message = client.messages.create(
    body=str(weather1),
    from_="+17816505199",
    to="+18152803280"
)

print(message.sid)













    



        

