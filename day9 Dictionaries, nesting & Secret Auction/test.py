'''dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
for key in dict:
    dict[key]+=1
print(dict)'''

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["dessert"][1])