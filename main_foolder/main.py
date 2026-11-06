import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrels_count)
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon_squirrels_count)
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)



# import csv

# with open("/Users/apple/umeraziz/pandas-python-csv/weather_data.csv", newline="") as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(row[1])

# print(tempratures)

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# biggest = data["temp"].max()
# print(biggest)

# print(data['condition'])
# print(data.condition)
# print(data[data.day ==  'Monday'])
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])
# monday = data[data.day == "Monday"]
# C = monday["temp"]
# F = C*(9/5)
# F += 32
# print(F)


# umer = type(data)
# print(umer)
# print(data['temp'])

# print(umer)


# data_dict = data.to_dict()
# print(data_dict)

# data_list = data['temp'].to_list()
# print(len(data_list))
# average = sum(data_list) / len(data_list)
# print(f'the average of data_list is {average}')
# avg = data["temp"].mean()
# print(avg)


# data_dict = {
#     "students" : ["amy" , "James" , "Angela"] ,
#     "scores": [76, 75, 65]
# }

# dic = pd.DataFrame(data_dict)
# dic.to_csv("new_data2.csv")
