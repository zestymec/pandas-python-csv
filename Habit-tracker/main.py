import time
import requests
from datetime import *

# today = datetime.now()
today = datetime(year=2026 , month= 9 , day= 17)



pixela_endpoint = "https://pixe.la/v1/users"

#  "token" : "8964fkbjdy89r32",
#     "username" : "umer",
#     "agreeTermsOfService" : "yes",
# UserName = "umera"
# Token = "8964fkbjdy89r32s" example


# user_params = {
#     "token" : Token ,
#     "username" : UserName,
#     "agreeTermsOfService" : "yes",
#     "notMinor" :  "yes",
#     # "thanksCode" : "" optional read pixela documentation
# }
# response = requests.post(url= pixela_endpoint , json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{UserName}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": Token,
}

# graph_response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers
# )
# print(graph_response.status_code)
# print(graph_response.text)


# graph url : https://pixe.la/v1/users/umera/graphs/graph1.html
print(
    f"Graph URL: https://pixe.la/v1/users/{UserName}/graphs/{graph_config['id']}.html"
)

postpixel_endpoint = f"{pixela_endpoint}/{UserName}/graphs/{graph_config['id']}"

postpixel_config = {
    "date": today.strftime("%Y%m%d") , 
    "quantity": "1.0",  # Old: "1" (float type ke liye "1.0" behtar hai)
}

# Purana single-attempt code:
# response_post = requests.post(
#     url=postpixel_endpoint,
#     json=postpixel_config,
#     headers=headers
# )
# print(response_post.status_code)
# print(response_post.text)

update_endpoint = f"{pixela_endpoint}/{UserName}/graphs/{graph_config['id']}/{today.strftime("%Y%m%d")}"
new_pixel_data = {
    "quantity" : "4.5"

}
# response = requests.put(url=update_endpoint , json=new_pixel_data ,headers=headers)
# print(response.text)





delet_endpoint = f"{pixela_endpoint}/{UserName}/graphs/{graph_config['id']}/{today.strftime("%Y%m%d")}"
response = requests.put(url=delet_endpoint , headers=headers)
print(response.text)
while True:
    response = requests.delete(url=delet_endpoint, headers=headers)
    print(response.status_code, response.text)

    if response.status_code == 200:
        print("✅ Pixel deleted!")
        break

    time.sleep(1)
# while True:
#     response_post = requests.post(
#         url=postpixel_endpoint, json=postpixel_config, headers=headers
#     )
#     print(response_post.status_code)
#     print(response_post.text)

#     if response_post.status_code == 200:
#         print("✅ Pixel successfully add ho gaya!")
#         break

#     time.sleep(1)

# Pixel banane ke liye Pixela Supporter program join karna hoga. Warna Pixela par new pixels create nahi honge.