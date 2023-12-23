import csv

with open('data_state.csv', newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]

print(data)