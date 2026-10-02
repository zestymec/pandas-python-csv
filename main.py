# import csv

# with open("/Users/apple/umeraziz/pandas-python-csv/weather_data.csv", newline="") as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(row[1])

# print(tempratures)

import pandas as pd

data_pd = pd.read_csv("weather_data.csv")
print(data_pd['temp'])

  