import requests
from datetime import datetime

my_lat = 52
my_lang = -1

parameters = {
    "lat" : my_lat , 
    "lng" : my_lang , 
    "formatted" :0
    }
response = requests.get(url="https://api.sunrise-sunset.org/json" , params= parameters)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunrise.split("T")[1].split(":")[0])
