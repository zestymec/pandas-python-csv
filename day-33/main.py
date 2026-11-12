import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # response.raise_for_status() 

# data = response.json()  
# print(data)
# # {
# # "timestamp": 1794465164,
# # "message": "success",
# # "iss_position": {
# # "longitude": "81.5528",
# # "latitude": "-45.6136"
# # }
# # }
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


# time_now = datetime.now()

# print(time_now)