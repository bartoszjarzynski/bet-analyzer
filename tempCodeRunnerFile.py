import json

with open('database.json', 'r') as file:
    data = json.load(file)

    data_length = len(data['data']) + 1
    print(data_length)