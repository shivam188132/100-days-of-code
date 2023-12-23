import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_Squirrels_count = len((data[data["Primary Fur Color"] == "Gray"]))
Cinnamon_Squirrels_count = len((data[data["Primary Fur Color"] == "Cinnamon"]))
Black_Squirrels_count = len((data[data["Primary Fur Color"] == "Black"]))

print(grey_Squirrels_count)
print(Cinnamon_Squirrels_count)
print(Black_Squirrels_count)

data_dict = {
    "color": ["Gray", "Cinnamon", "Black"],
    "count": [grey_Squirrels_count, Cinnamon_Squirrels_count, Black_Squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrels_count.csv")
