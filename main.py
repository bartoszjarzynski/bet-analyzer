import json


Aston_Villa_Points = [0 , 0, 0, 0, 0, 0]
Brighton_Points = [0, 0, 0, 0, 0, 0]
Man_United_Points = [0, 0, 0, 0, 0, 0]
Crystal_Palace_Points = [0, 0, 0, 0, 0, 0]
Newcastle_Points = [0, 0, 0, 0, 0, 0]
Burnley_Points = [0, 0, 0, 0, 0, 0]
Wolves_Points = [0, 0, 0, 0, 0, 0]
Man_City_Points = [0, 0, 0, 0, 0, 0]
Bournemouth_Points = [0, 0, 0, 0, 0, 0]
Arsenal_Points = [0, 0, 0, 0, 0, 0]
West_ham_Points = [0, 0, 0, 0, 0, 0]
Sheffield_Points = [0, 0, 0, 0, 0, 0]
Everton_Points = [0, 0, 0, 0, 0, 0]
Luton_Points = [0, 0, 0, 0, 0, 0]
Tottenham_Points = [0, 0, 0, 0, 0, 0]
Liverpool_Points = [0, 0, 0, 0, 0, 0]
Nottingham_Points = [0, 0, 0, 0, 0, 0]
Brentford_Points = [0, 0, 0, 0, 0, 0]
Fulham_Points = [0, 0, 0, 0, 0, 0]
Chelsea_Points = [0, 0, 0, 0, 0, 0]



with open('database.json', 'r') as file:
    data = json.load(file)

    # Printing length of data here
    data_length = len(data['data'])
    print(data_length)
    
    # Printing all the data from database.json
    print(json.dumps(data, indent=4))
    
    # Printing first match (index: 0) database.json
    print(json.dumps(data['data'][0], indent=4))



    for i in range(data_length):
        if data["data"][i]["home_goals"]>data["data"][i]["away_goals"]:
            if data["data"][i]["home_team"] == "Aston Villa":
                Aston_Villa_Points[0]=Aston_Villa_Points[0]+3
            elif data["data"][i]["home_team"] == "Brighton":
                Brighton_Points[0]=Brighton_Points[0]+3
            elif data["data"][i]["home_team"] == "Man United":
                Man_United_Points[0]=Man_United_Points[0]+3
            elif data["data"][i]["home_team"] == "Crystal Palace":
                Crystal_Palace_Points[0]=Crystal_Palace_Points[0]+3
            elif data["data"][i]["home_team"] == "Newcastle":
                Newcastle_Points[0]=Newcastle_Points[0]+3
            elif data["data"][i]["home_team"] == "Burnley":
                Burnley_Points[0]=Burnley_Points[0]+3
            elif data["data"][i]["home_team"] == "Wolves":
                Wolves_Points[0]=Wolves_Points[0]+3
            elif data["data"][i]["home_team"] == "Man City":
                Man_City_Points[0]=Man_City_Points[0]+3
            elif data["data"][i]["home_team"] == "Bournemouth":
                Bournemouth_Points[0]=Bournemouth_Points[0]+3
            elif data["data"][i]["home_team"] == "Arsenal":
                Arsenal_Points[0]=Arsenal_Points[0]+3
            elif data["data"][i]["home_team"] == "West_Ham":
                West_ham_Points[0]=West_ham_Points[0]+3
            elif data["data"][i]["home_team"] == "Sheffield":
                Sheffield_Points[0]=Sheffield_Points[0]+3
            elif data["data"][i]["home_team"] == "Everton":
                Everton_Points[0]=Everton_Points[0]+3
            elif data["data"][i]["home_team"] == "Luton":
                Luton_Points[0]=Luton_Points[0]+3
            elif data["data"][i]["home_team"] == "Tottenham":
                Tottenham_Points[0]=Tottenham_Points[0]+3
            elif data["data"][i]["home_team"] == "Liverpool":
                Liverpool_Points[0]=Liverpool_Points[0]+3
            elif data["data"][i]["home_team"] == "Nottingham":
                Nottingham_Points[0]=Nottingham_Points[0]+3
            elif data["data"][i]["home_team"] == "Brentford":
                Brentford_Points[0]=Brentford_Points[0]+3
            elif data["data"][i]["home_team"] == "Fulham":
                Fulham_Points[0]=Fulham_Points[0]+3
            elif data["data"][i]["home_team"] == "Chelsea":
                Chelsea_Points[0]=Chelsea_Points[0]+3

        if data["data"][i]["home_goals"]<data["data"][i]["away_goals"]:
            if data["data"][i]["away_team"] == "Aston Villa":
                Aston_Villa_Points[0]=Aston_Villa_Points[0]+3
            elif data["data"][i]["away_team"] == "Brighton":
                Brighton_Points[0]=Brighton_Points[0]+3
            elif data["data"][i]["away_team"] == "Man United":
                Man_United_Points[0]=Man_United_Points[0]+3
            elif data["data"][i]["away_team"] == "Crystal Palace":
                Crystal_Palace_Points[0]=Crystal_Palace_Points[0]+3
            elif data["data"][i]["away_team"] == "Newcastle":
                Newcastle_Points[0]=Newcastle_Points[0]+3
            elif data["data"][i]["away_team"] == "Burnley":
                Burnley_Points[0]=Burnley_Points[0]+3
            elif data["data"][i]["away_team"] == "Wolves":
                Wolves_Points[0]=Wolves_Points[0]+3
            elif data["data"][i]["away_team"] == "Man City":
                Man_City_Points[0]=Man_City_Points[0]+3
            elif data["data"][i]["away_team"] == "Bournemouth":
                Bournemouth_Points[0]=Bournemouth_Points[0]+3
            elif data["data"][i]["away_team"] == "Arsenal":
                Arsenal_Points[0]=Arsenal_Points[0]+3
            elif data["data"][i]["away_team"] == "West_Ham":
                West_ham_Points[0]=West_ham_Points[0]+3
            elif data["data"][i]["away_team"] == "Sheffield":
                Sheffield_Points[0]=Sheffield_Points[0]+3
            elif data["data"][i]["away_team"] == "Everton":
                Everton_Points[0]=Everton_Points[0]+3
            elif data["data"][i]["away_team"] == "Luton":
                Luton_Points[0]=Luton_Points[0]+3
            elif data["data"][i]["away_team"] == "Tottenham":
                Tottenham_Points[0]=Tottenham_Points[0]+3
            elif data["data"][i]["away_team"] == "Liverpool":
                Liverpool_Points[0]=Liverpool_Points[0]+3
            elif data["data"][i]["away_team"] == "Nottingham":
                Nottingham_Points[0]=Nottingham_Points[0]+3
            elif data["data"][i]["away_team"] == "Brentford":
                Brentford_Points[0]=Brentford_Points[0]+3
            elif data["data"][i]["away_team"] == "Fulham":
                Fulham_Points[0]=Fulham_Points[0]+3
            elif data["data"][i]["away_team"] == "Chelsea":
                Chelsea_Points[0]=Chelsea_Points[0]+3

        if data["data"][i]["home_goals"]==data["data"][i]["away_goals"]:
            if data["data"][i]["away_team"] == "Aston Villa":
                Aston_Villa_Points[0]=Aston_Villa_Points[0]+1
            if data["data"][i]["away_team"] == "Brighton":
                Brighton_Points[0]=Brighton_Points[0]+1
            if data["data"][i]["away_team"] == "Man United":
                Man_United_Points[0]=Man_United_Points[0]+1
            if data["data"][i]["away_team"] == "Crystal Palace":
                Crystal_Palace_Points[0]=Crystal_Palace_Points[0]+1
            if data["data"][i]["away_team"] == "Newcastle":
                Newcastle_Points[0]=Newcastle_Points[0]+1
            if data["data"][i]["away_team"] == "Burnley":
                Burnley_Points[0]=Burnley_Points[0]+1
            if data["data"][i]["away_team"] == "Wolves":
                Wolves_Points[0]=Wolves_Points[0]+1
            if data["data"][i]["away_team"] == "Man City":
                Man_City_Points[0]=Man_City_Points[0]+1
            if data["data"][i]["away_team"] == "Bournemouth":
                Bournemouth_Points[0]=Bournemouth_Points[0]+1
            if data["data"][i]["away_team"] == "Arsenal":
                Arsenal_Points[0]=Arsenal_Points[0]+1
            if data["data"][i]["away_team"] == "West_Ham":
                West_ham_Points[0]=West_ham_Points[0]+1
            if data["data"][i]["away_team"] == "Sheffield":
                Sheffield_Points[0]=Sheffield_Points[0]+1
            if data["data"][i]["away_team"] == "Everton":
                Everton_Points[0]=Everton_Points[0]+1
            if data["data"][i]["away_team"] == "Luton":
                Luton_Points[0]=Luton_Points[0]+1
            if data["data"][i]["away_team"] == "Tottenham":
                Tottenham_Points[0]=Tottenham_Points[0]+1
            if data["data"][i]["away_team"] == "Liverpool":
                Liverpool_Points[0]=Liverpool_Points[0]+1
            if data["data"][i]["away_team"] == "Nottingham":
                Nottingham_Points[0]=Nottingham_Points[0]+1
            if data["data"][i]["away_team"] == "Brentford":
                Brentford_Points[0]=Brentford_Points[0]+1
            if data["data"][i]["away_team"] == "Fulham":
                Fulham_Points[0]=Fulham_Points[0]+1
            if data["data"][i]["away_team"] == "Chelsea":
                Chelsea_Points[0]=Chelsea_Points[0]+1 
            if data["data"][i]["home_team"] == "Aston Villa":
                Aston_Villa_Points[0]=Aston_Villa_Points[0]+1
            if data["data"][i]["home_team"] == "Brighton":
                Brighton_Points[0]=Brighton_Points[0]+1
            if data["data"][i]["home_team"] == "Man United":
                Man_United_Points[0]=Man_United_Points[0]+1
            if data["data"][i]["home_team"] == "Crystal Palace":
                Crystal_Palace_Points[0]=Crystal_Palace_Points[0]+1
            if data["data"][i]["home_team"] == "Newcastle":
                Newcastle_Points[0]=Newcastle_Points[0]+1
            if data["data"][i]["home_team"] == "Burnley":
                Burnley_Points[0]=Burnley_Points[0]+1
            if data["data"][i]["home_team"] == "Wolves":
                Wolves_Points[0]=Wolves_Points[0]+1
            if data["data"][i]["home_team"] == "Man City":
                Man_City_Points[0]=Man_City_Points[0]+1
            if data["data"][i]["home_team"] == "Bournemouth":
                Bournemouth_Points[0]=Bournemouth_Points[0]+1
            if data["data"][i]["home_team"] == "Arsenal":
                Arsenal_Points[0]=Arsenal_Points[0]+1
            if data["data"][i]["home_team"] == "West_Ham":
                West_ham_Points[0]=West_ham_Points[0]+1
            if data["data"][i]["home_team"] == "Sheffield":
                Sheffield_Points[0]=Sheffield_Points[0]+3
            if data["data"][i]["home_team"] == "Everton":
                Everton_Points[0]=Everton_Points[0]+1
            if data["data"][i]["home_team"] == "Luton":
                Luton_Points[0]=Luton_Points[0]+1
            if data["data"][i]["home_team"] == "Tottenham":
                Tottenham_Points[0]=Tottenham_Points[0]+1
            if data["data"][i]["home_team"] == "Liverpool":
                Liverpool_Points[0]=Liverpool_Points[0]+1
            if data["data"][i]["home_team"] == "Nottingham":
                Nottingham_Points[0]=Nottingham_Points[0]+1
            if data["data"][i]["home_team"] == "Brentford":
                Brentford_Points[0]=Brentford_Points[0]+1
            if data["data"][i]["home_team"] == "Fulham":
                Fulham_Points[0]=Fulham_Points[0]+1
            if data["data"][i]["home_team"] == "Chelsea":
                Chelsea_Points[0]=Chelsea_Points[0]+1


    print(Aston_Villa_Points)
    

    





