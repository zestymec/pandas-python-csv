import requests

pixela_endpoint = "https://pixe.la/v1/users"

#  "token" : "8964fkbjdy89r32",
#     "username" : "umer",
#     "agreeTermsOfService" : "yes",
UserName = "umera"
Token = "8964fkbjdy89r32s"
user_params = {
    "token" : Token , 
    "username" : UserName,
    "agreeTermsOfService" : "yes",
    "notMinor" :  "yes",
    # "thanksCode" : "" optional read pixela documentation

}

response = requests.post(url= pixela_endpoint , json=user_params)

print(response.text)

graph_endpoint = f"{pixela_endpoint}/{UserName}/graphs"
graph_config = {
    "id" : "graph1",
    "name" : "Cycling Graph" ,
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai",

}
headers = {
    "X-USER-TOKEN" : Token,
}

graph_response = requests.post(
    url=graph_endpoint,
    json=graph_config,
    headers=headers
)

print(graph_response.status_code)
print(graph_response.text)


# graph url : https://pixe.la/v1/users/umera/graphs/graph1.html

print(f"Graph URL: https://pixe.la/v1/users/{UserName}/graphs/{graph_config['id']}.html")


postpixel_endpoint = (
    f"{pixela_endpoint}/{UserName}/graphs/{graph_config['id']}/pixels"
)


postpixel_config = {
    "date": "20261117",
    "quantity": "1"
}

response_post = requests.post(
    url=postpixel_endpoint,
    json=postpixel_config,
    headers=headers
)

print(response_post.status_code)
print(response_post.text)


# Pixel banane ke liye Pixela Supporter program join karna hoga. Warna Pixela par new pixels create nahi honge.

