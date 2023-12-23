"""with open(".\weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)"""
"""temperature = []
import csv

with open(".\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # print(data)

    for row in data:
        #print(row)
        if row[1] != "temp":
            #temperature.append((row[1]))
            temperature.append(int((row[1])))
        # print(row[1])

print(temperature)"""

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# # print in dictionary
# data_dict = data.to_dict()
# print(data_dict)
# # to print temp as list in column format
# temp_list = data["temp"].to_list()
# print(temp_list)
# # print avg temperature
# avg_temp = round(sum(temp_list)/len(temp_list), 2)
# print(avg_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
# # get data in column
# print(data.condition)
# print(data["condition"])
# get data in rows
# print(data[data["day"] == "Monday"])
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp)
# # convert monday temp in  farenheight
# print(f"{monday.temp*9/5 + 32} farenheight" )
#  create a dataframe from scratch
data_dict = {
    "students" : ["Ajay", "Shivam", "Raj kishore"],
    "scores"   : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)