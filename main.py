import json

with open('database.json', 'r') as file:
    data = json.load(file)

    # Printing length of data here
    data_length = len(data['data'])
    print(data_length)
    
    # Printing all the data from database.json
    print(json.dumps(data, indent=4))
    
    # Printing first match (index: 0) database.json
    print(json.dumps(data['data'][0], indent=4))