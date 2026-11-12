import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status() 

data = response.json()  
print(data)
# {
# "timestamp": 1794465164,
# "message": "success",
# "iss_position": {
# "longitude": "81.5528",
# "latitude": "-45.6136"
# }
# }