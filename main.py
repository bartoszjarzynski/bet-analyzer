import json

# punkty/punkty u siebie/punkty na wyjezdzie/gole strzelone/gole stracone/forma 5/forma10
Aston_Villa_Points = [0 , 0, 0, 0, 0, 0, 0]
Brighton_Points = [0, 0, 0, 0, 0, 0, 0]
Man_United_Points = [0, 0, 0, 0, 0, 0, 0]
Crystal_Palace_Points = [0, 0, 0, 0, 0, 0, 0]
Newcastle_Points = [0, 0, 0, 0, 0, 0, 0]
Burnley_Points = [0, 0, 0, 0, 0, 0, 0]
Wolves_Points = [0, 0, 0, 0, 0, 0, 0]
Man_City_Points = [0, 0, 0, 0, 0, 0, 0]
Bournemouth_Points = [0, 0, 0, 0, 0, 0, 0]
Arsenal_Points = [0, 0, 0, 0, 0, 0, 0]
West_ham_Points = [0, 0, 0, 0, 0, 0, 0]
Sheffield_Points = [0, 0, 0, 0, 0, 0, 0]
Everton_Points = [0, 0, 0, 0, 0, 0, 0]
Luton_Points = [0, 0, 0, 0, 0, 0, 0]
Tottenham_Points = [0, 0, 0, 0, 0, 0, 0]
Liverpool_Points = [0, 0, 0, 0, 0, 0, 0]
Nottingham_Points = [0, 0, 0, 0, 0, 0, 0]
Brentford_Points = [0, 0, 0, 0, 0, 0, 0]
Fulham_Points = [0, 0, 0, 0, 0, 0, 0]
Chelsea_Points = [0, 0, 0, 0, 0, 0, 0]



with open('database.json', 'r') as file:
    data = json.load(file)

    # Printing length of data here
    data_length = len(data['data'])
    #print(data_length)
    
    # Printing all the data from database.json
    #print(json.dumps(data, indent=4))
    
    # Printing first match (index: 0) database.json
    #print(json.dumps(data['data'][0], indent=4))

    last_round=int(data["data"][data_length-1]["round "])
    #print(last_round)


    for i in range(data_length):
        ##Punkty/Punkty u siebie/Punkty na wyjezdzie
        if data["data"][i]["home_goals"]>data["data"][i]["away_goals"]:
            if data["data"][i]["home_team"] == "Aston Villa":
                Aston_Villa_Points[0]=Aston_Villa_Points[0]+3
                Aston_Villa_Points[1]=Aston_Villa_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                    Aston_Villa_Points[5]=Aston_Villa_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Aston_Villa_Points[6]=Aston_Villa_Points[6]+3
            elif data["data"][i]["home_team"] == "Brighton":
                Brighton_Points[0]=Brighton_Points[0]+3
                Brighton_Points[1]=Brighton_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Brighton_Points[5]=Brighton_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Brighton_Points[6]=Brighton_Points[6]+3
            elif data["data"][i]["home_team"] == "Man United":
                Man_United_Points[0]=Man_United_Points[0]+3
                Man_United_Points[1]=Man_United_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Man_United_Points[5]=Man_United_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Man_United_Points[6]=Man_United_Points[6]+3
            elif data["data"][i]["home_team"] == "Crystal Palace":
                Crystal_Palace_Points[0]=Crystal_Palace_Points[0]+3
                Crystal_Palace_Points[1]=Crystal_Palace_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Crystal_Palace_Points[5]=Crystal_Palace_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Crystal_Palace_Points[6]=Crystal_Palace_Points[6]+3
            elif data["data"][i]["home_team"] == "Newcastle":
                Newcastle_Points[0]=Newcastle_Points[0]+3
                Newcastle_Points[1]=Newcastle_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Newcastle_Points[5]=Newcastle_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Newcastle_Points[6]=Newcastle_Points[6]+3
            elif data["data"][i]["home_team"] == "Burnley":
                Burnley_Points[0]=Burnley_Points[0]+3
                Burnley_Points[1]=Burnley_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                    Burnley_Points[5]=Burnley_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Burnley_Points[6]=Burnley_Points[6]+3
            elif data["data"][i]["home_team"] == "Wolves":
                Wolves_Points[0]=Wolves_Points[0]+3
                Wolves_Points[1]=Wolves_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Wolves_Points[5]=Wolves_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Wolves_Points[6]=Wolves_Points[6]+3
            elif data["data"][i]["home_team"] == "Man City":
                Man_City_Points[0]=Man_City_Points[0]+3
                Man_City_Points[1]=Man_City_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Man_City_Points[5]=Man_City_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Man_City_Points[6]=Man_City_Points[6]+3
            elif data["data"][i]["home_team"] == "Bournemouth":
                Bournemouth_Points[0]=Bournemouth_Points[0]+3
                Bournemouth_Points[1]=Bournemouth_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Bournemouth_Points[5]=Bournemouth_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Bournemouth_Points[6]=Bournemouth_Points[6]+3
            elif data["data"][i]["home_team"] == "Arsenal":
                Arsenal_Points[0]=Arsenal_Points[0]+3
                Arsenal_Points[1]=Arsenal_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Arsenal_Points[5]=Arsenal_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Arsenal_Points[6]=Arsenal_Points[6]+3
            elif data["data"][i]["home_team"] == "West Ham":
                West_ham_Points[0]=West_ham_Points[0]+3
                West_ham_Points[1]=West_ham_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     West_ham_Points[5]=West_ham_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     West_ham_Points[6]=West_ham_Points[6]+3
            elif data["data"][i]["home_team"] == "Sheffield":
                Sheffield_Points[0]=Sheffield_Points[0]+3
                Sheffield_Points[1]=Sheffield_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Sheffield_Points[5]=Sheffield_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Sheffield_Points[6]=Sheffield_Points[6]+3
            elif data["data"][i]["home_team"] == "Everton":
                Everton_Points[0]=Everton_Points[0]+3
                Everton_Points[1]=Everton_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Everton_Points[5]=Everton_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Everton_Points[6]=Everton_Points[6]+3
            elif data["data"][i]["home_team"] == "Luton":
                Luton_Points[0]=Luton_Points[0]+3
                Luton_Points[1]=Luton_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Luton_Points[5]=Luton_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Luton_Points[6]=Luton_Points[6]+3
            elif data["data"][i]["home_team"] == "Tottenham":
                Tottenham_Points[0]=Tottenham_Points[0]+3
                Tottenham_Points[1]=Tottenham_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Tottenham_Points[5]=Tottenham_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Tottenham_Points[6]=Tottenham_Points[6]+3
            elif data["data"][i]["home_team"] == "Liverpool":
                Liverpool_Points[0]=Liverpool_Points[0]+3
                Liverpool_Points[1]=Liverpool_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Liverpool_Points[5]=Liverpool_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Liverpool_Points[6]=Liverpool_Points[6]+3
            elif data["data"][i]["home_team"] == "Nottingham":
                Nottingham_Points[0]=Nottingham_Points[0]+3
                Nottingham_Points[1]=Nottingham_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Nottingham_Points[5]=Nottingham_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Nottingham_Points[6]=Nottingham_Points[6]+3
            elif data["data"][i]["home_team"] == "Brentford":
                Brentford_Points[0]=Brentford_Points[0]+3
                Brentford_Points[1]=Brentford_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Brentford_Points[5]=Brentford_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Brentford_Points[6]=Brentford_Points[6]+3
            elif data["data"][i]["home_team"] == "Fulham":
                Fulham_Points[0]=Fulham_Points[0]+3
                Fulham_Points[1]=Fulham_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Fulham_Points[5]=Fulham_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Fulham_Points[6]=Fulham_Points[6]+3
            elif data["data"][i]["home_team"] == "Chelsea":
                Chelsea_Points[0]=Chelsea_Points[0]+3
                Chelsea_Points[1]=Chelsea_Points[1]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Chelsea_Points[5]=Chelsea_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Chelsea_Points[6]=Chelsea_Points[6]+3


        if data["data"][i]["home_goals"]<data["data"][i]["away_goals"]:
            if data["data"][i]["away_team"] == "Aston Villa":
                Aston_Villa_Points[0]=Aston_Villa_Points[0]+3
                Aston_Villa_Points[2]=Aston_Villa_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Aston_Villa_Points[5]=Aston_Villa_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Aston_Villa_Points[6]=Aston_Villa_Points[6]+3
            elif data["data"][i]["away_team"] == "Brighton":
                Brighton_Points[0]=Brighton_Points[0]+3
                Brighton_Points[2]=Brighton_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Brighton_Points[5]=Brighton_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Brighton_Points[6]=Brighton_Points[6]+3
            elif data["data"][i]["away_team"] == "Man United":
                Man_United_Points[0]=Man_United_Points[0]+3
                Man_United_Points[2]=Man_United_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Man_United_Points[5]=Man_United_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Man_United_Points[6]=Man_United_Points[6]+3
            elif data["data"][i]["away_team"] == "Crystal Palace":
                Crystal_Palace_Points[0]=Crystal_Palace_Points[0]+3
                Crystal_Palace_Points[2]=Crystal_Palace_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Crystal_Palace_Points[5]=Crystal_Palace_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Crystal_Palace_Points[6]=Crystal_Palace_Points[6]+3
            elif data["data"][i]["away_team"] == "Newcastle":
                Newcastle_Points[0]=Newcastle_Points[0]+3
                Newcastle_Points[2]=Newcastle_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Newcastle_Points[5]=Newcastle_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Newcastle_Points[6]=Newcastle_Points[6]+3
            elif data["data"][i]["away_team"] == "Burnley":
                Burnley_Points[0]=Burnley_Points[0]+3
                Burnley_Points[2]=Burnley_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Burnley_Points[5]=Burnley_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Burnley_Points[6]=Burnley_Points[6]+3
            elif data["data"][i]["away_team"] == "Wolves":
                Wolves_Points[0]=Wolves_Points[0]+3
                Wolves_Points[2]=Wolves_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Wolves_Points[5]=Wolves_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Wolves_Points[6]=Wolves_Points[6]+3
            elif data["data"][i]["away_team"] == "Man City":
                Man_City_Points[0]=Man_City_Points[0]+3
                Man_City_Points[2]=Man_City_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Man_City_Points[5]=Man_City_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Man_City_Points[6]=Man_City_Points[6]+3
            elif data["data"][i]["away_team"] == "Bournemouth":
                Bournemouth_Points[0]=Bournemouth_Points[0]+3
                Bournemouth_Points[2]=Bournemouth_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Bournemouth_Points[5]=Bournemouth_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Bournemouth_Points[6]=Bournemouth_Points[6]+3
            elif data["data"][i]["away_team"] == "Arsenal":
                Arsenal_Points[0]=Arsenal_Points[0]+3
                Arsenal_Points[2]=Arsenal_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Arsenal_Points[5]=Arsenal_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Arsenal_Points[6]=Arsenal_Points[6]+3
            elif data["data"][i]["away_team"] == "West Ham":
                West_ham_Points[0]=West_ham_Points[0]+3
                West_ham_Points[2]=West_ham_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     West_ham_Points[5]=West_ham_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     West_ham_Points[6]=West_ham_Points[6]+3
            elif data["data"][i]["away_team"] == "Sheffield":
                Sheffield_Points[0]=Sheffield_Points[0]+3
                Sheffield_Points[2]=Sheffield_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Sheffield_Points[5]=Sheffield_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Sheffield_Points[6]=Sheffield_Points[6]+3
            elif data["data"][i]["away_team"] == "Everton":
                Everton_Points[0]=Everton_Points[0]+3
                Everton_Points[2]=Everton_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Everton_Points[5]=Everton_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Everton_Points[6]=Everton_Points[6]+3
            elif data["data"][i]["away_team"] == "Luton":
                Luton_Points[0]=Luton_Points[0]+3
                Luton_Points[2]=Luton_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Luton_Points[5]=Luton_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Luton_Points[6]=Luton_Points[6]+3
            elif data["data"][i]["away_team"] == "Tottenham":
                Tottenham_Points[0]=Tottenham_Points[0]+3
                Tottenham_Points[2]=Tottenham_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Tottenham_Points[5]=Tottenham_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Tottenham_Points[6]=Tottenham_Points[6]+3
            elif data["data"][i]["away_team"] == "Liverpool":
                Liverpool_Points[0]=Liverpool_Points[0]+3
                Liverpool_Points[2]=Liverpool_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Liverpool_Points[5]=Liverpool_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Liverpool_Points[6]=Liverpool_Points[6]+3
            elif data["data"][i]["away_team"] == "Nottingham":
                Nottingham_Points[0]=Nottingham_Points[0]+3
                Nottingham_Points[2]=Nottingham_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Nottingham_Points[5]=Nottingham_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Nottingham_Points[6]=Nottingham_Points[6]+3
            elif data["data"][i]["away_team"] == "Brentford":
                Brentford_Points[0]=Brentford_Points[0]+3
                Brentford_Points[2]=Brentford_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Brentford_Points[5]=Brentford_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Brentford_Points[6]=Brentford_Points[6]+3
            elif data["data"][i]["away_team"] == "Fulham":
                Fulham_Points[0]=Fulham_Points[0]+3
                Fulham_Points[2]=Fulham_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Fulham_Points[5]=Fulham_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Fulham_Points[6]=Fulham_Points[6]+3
            elif data["data"][i]["away_team"] == "Chelsea":
                Chelsea_Points[0]=Chelsea_Points[0]+3
                Chelsea_Points[2]=Chelsea_Points[2]+3
                if int(data["data"][i]["round "])>=last_round-4:
                     Chelsea_Points[5]=Chelsea_Points[5]+3
                if int(data["data"][i]["round "])>=last_round-9:
                     Chelsea_Points[6]=Chelsea_Points[6]+3



        if data["data"][i]["home_goals"]==data["data"][i]["away_goals"]:
            if data["data"][i]["away_team"] == "Aston Villa":
                Aston_Villa_Points[0]=Aston_Villa_Points[0]+1
                Aston_Villa_Points[2]=Aston_Villa_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Aston_Villa_Points[5]=Aston_Villa_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Aston_Villa_Points[6]=Aston_Villa_Points[6]+1
            if data["data"][i]["away_team"] == "Brighton":
                Brighton_Points[0]=Brighton_Points[0]+1
                Brighton_Points[2]=Brighton_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Brighton_Points[5]=Brighton_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Brighton_Points[6]=Brighton_Points[6]+1
            if data["data"][i]["away_team"] == "Man United":
                Man_United_Points[0]=Man_United_Points[0]+1
                Man_United_Points[2]=Man_United_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Man_United_Points[5]=Man_United_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Man_United_Points[6]=Man_United_Points[6]+1
            if data["data"][i]["away_team"] == "Crystal Palace":
                Crystal_Palace_Points[0]=Crystal_Palace_Points[0]+1
                Crystal_Palace_Points[2]=Crystal_Palace_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Crystal_Palace_Points[5]=Crystal_Palace_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Crystal_Palace_Points[6]=Crystal_Palace_Points[6]+1
            if data["data"][i]["away_team"] == "Newcastle":
                Newcastle_Points[0]=Newcastle_Points[0]+1
                Newcastle_Points[2]=Newcastle_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Newcastle_Points[5]=Newcastle_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Newcastle_Points[6]=Newcastle_Points[6]+1
            if data["data"][i]["away_team"] == "Burnley":
                Burnley_Points[0]=Burnley_Points[0]+1
                Burnley_Points[2]=Burnley_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Burnley_Points[5]=Burnley_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Burnley_Points[6]=Burnley_Points[6]+1
            if data["data"][i]["away_team"] == "Wolves":
                Wolves_Points[0]=Wolves_Points[0]+1
                Wolves_Points[2]=Wolves_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Wolves_Points[5]=Wolves_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Wolves_Points[6]=Wolves_Points[6]+1
            if data["data"][i]["away_team"] == "Man City":
                Man_City_Points[0]=Man_City_Points[0]+1
                Man_City_Points[2]=Man_City_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Man_City_Points[5]=Man_City_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Man_City_Points[6]=Man_City_Points[6]+1
            if data["data"][i]["away_team"] == "Bournemouth":
                Bournemouth_Points[0]=Bournemouth_Points[0]+1
                Bournemouth_Points[2]=Bournemouth_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Bournemouth_Points[5]=Bournemouth_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Bournemouth_Points[6]=Bournemouth_Points[6]+1
            if data["data"][i]["away_team"] == "Arsenal":
                Arsenal_Points[0]=Arsenal_Points[0]+1
                Arsenal_Points[2]=Arsenal_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Arsenal_Points[5]=Arsenal_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Arsenal_Points[6]=Arsenal_Points[6]+1
            if data["data"][i]["away_team"] == "West Ham":
                West_ham_Points[0]=West_ham_Points[0]+1
                West_ham_Points[2]=West_ham_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     West_ham_Points[5]=West_ham_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     West_ham_Points[6]=West_ham_Points[6]+1
            if data["data"][i]["away_team"] == "Sheffield":
                Sheffield_Points[0]=Sheffield_Points[0]+1
                Sheffield_Points[2]=Sheffield_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Sheffield_Points[5]=Sheffield_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Sheffield_Points[6]=Sheffield_Points[6]+1
            if data["data"][i]["away_team"] == "Everton":
                Everton_Points[0]=Everton_Points[0]+1
                Everton_Points[2]=Everton_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Everton_Points[5]=Everton_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Everton_Points[6]=Everton_Points[6]+1
            if data["data"][i]["away_team"] == "Luton":
                Luton_Points[0]=Luton_Points[0]+1
                Luton_Points[2]=Luton_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Luton_Points[5]=Luton_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Luton_Points[6]=Luton_Points[6]+1
            if data["data"][i]["away_team"] == "Tottenham":
                Tottenham_Points[0]=Tottenham_Points[0]+1
                Tottenham_Points[2]=Tottenham_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Tottenham_Points[5]=Tottenham_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Tottenham_Points[6]=Tottenham_Points[6]+1
            if data["data"][i]["away_team"] == "Liverpool":
                Liverpool_Points[0]=Liverpool_Points[0]+1
                Liverpool_Points[2]=Liverpool_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Liverpool_Points[5]=Liverpool_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Liverpool_Points[6]=Liverpool_Points[6]+1
            if data["data"][i]["away_team"] == "Nottingham":
                Nottingham_Points[0]=Nottingham_Points[0]+1
                Nottingham_Points[2]=Nottingham_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Nottingham_Points[5]=Nottingham_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Nottingham_Points[6]=Nottingham_Points[6]+1
            if data["data"][i]["away_team"] == "Brentford":
                Brentford_Points[0]=Brentford_Points[0]+1
                Brentford_Points[2]=Brentford_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Brentford_Points[5]=Brentford_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Brentford_Points[6]=Brentford_Points[6]+1
            if data["data"][i]["away_team"] == "Fulham":
                Fulham_Points[0]=Fulham_Points[0]+1
                Fulham_Points[2]=Fulham_Points[2]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Fulham_Points[5]=Fulham_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Fulham_Points[6]=Fulham_Points[6]+1
            if data["data"][i]["away_team"] == "Chelsea":
                Chelsea_Points[0]=Chelsea_Points[0]+1 
                Chelsea_Points[2]=Chelsea_Points[2]+1 
                if int(data["data"][i]["round "])>=last_round-4:
                     Chelsea_Points[5]=Chelsea_Points[5]+1 
                if int(data["data"][i]["round "])>=last_round-9:
                     Chelsea_Points[6]=Chelsea_Points[6]+1 
            if data["data"][i]["home_team"] == "Aston Villa":
                Aston_Villa_Points[0]=Aston_Villa_Points[0]+1
                Aston_Villa_Points[1]=Aston_Villa_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Aston_Villa_Points[5]=Aston_Villa_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Aston_Villa_Points[6]=Aston_Villa_Points[6]+1
            if data["data"][i]["home_team"] == "Brighton":
                Brighton_Points[0]=Brighton_Points[0]+1
                Brighton_Points[1]=Brighton_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Brighton_Points[5]=Brighton_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Brighton_Points[6]=Brighton_Points[6]+1
            if data["data"][i]["home_team"] == "Man United":
                Man_United_Points[0]=Man_United_Points[0]+1
                Man_United_Points[1]=Man_United_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Man_United_Points[5]=Man_United_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Man_United_Points[6]=Man_United_Points[6]+1
            if data["data"][i]["home_team"] == "Crystal Palace":
                Crystal_Palace_Points[0]=Crystal_Palace_Points[0]+1
                Crystal_Palace_Points[1]=Crystal_Palace_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Crystal_Palace_Points[5]=Crystal_Palace_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Crystal_Palace_Points[6]=Crystal_Palace_Points[6]+1
            if data["data"][i]["home_team"] == "Newcastle":
                Newcastle_Points[0]=Newcastle_Points[0]+1
                Newcastle_Points[1]=Newcastle_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Newcastle_Points[5]=Newcastle_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Newcastle_Points[6]=Newcastle_Points[6]+1
            if data["data"][i]["home_team"] == "Burnley":
                Burnley_Points[0]=Burnley_Points[0]+1
                Burnley_Points[1]=Burnley_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Burnley_Points[5]=Burnley_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Burnley_Points[6]=Burnley_Points[6]+1
            if data["data"][i]["home_team"] == "Wolves":
                Wolves_Points[0]=Wolves_Points[0]+1
                Wolves_Points[1]=Wolves_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Wolves_Points[5]=Wolves_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Wolves_Points[6]=Wolves_Points[6]+1
            if data["data"][i]["home_team"] == "Man City":
                Man_City_Points[0]=Man_City_Points[0]+1
                Man_City_Points[1]=Man_City_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Man_City_Points[5]=Man_City_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Man_City_Points[6]=Man_City_Points[6]+1
            if data["data"][i]["home_team"] == "Bournemouth":
                Bournemouth_Points[0]=Bournemouth_Points[0]+1
                Bournemouth_Points[1]=Bournemouth_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Bournemouth_Points[5]=Bournemouth_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Bournemouth_Points[6]=Bournemouth_Points[6]+1
            if data["data"][i]["home_team"] == "Arsenal":
                Arsenal_Points[0]=Arsenal_Points[0]+1
                Arsenal_Points[1]=Arsenal_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Arsenal_Points[5]=Arsenal_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Arsenal_Points[6]=Arsenal_Points[6]+1
            if data["data"][i]["home_team"] == "West Ham":
                West_ham_Points[0]=West_ham_Points[0]+1
                West_ham_Points[1]=West_ham_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     West_ham_Points[5]=West_ham_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     West_ham_Points[6]=West_ham_Points[6]+1
            if data["data"][i]["home_team"] == "Sheffield":
                Sheffield_Points[0]=Sheffield_Points[0]+1
                Sheffield_Points[1]=Sheffield_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Sheffield_Points[5]=Sheffield_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Sheffield_Points[6]=Sheffield_Points[6]+1
            if data["data"][i]["home_team"] == "Everton":
                Everton_Points[0]=Everton_Points[0]+1
                Everton_Points[1]=Everton_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Everton_Points[5]=Everton_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Everton_Points[6]=Everton_Points[6]+1
            if data["data"][i]["home_team"] == "Luton":
                Luton_Points[0]=Luton_Points[0]+1
                Luton_Points[1]=Luton_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Luton_Points[5]=Luton_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Luton_Points[6]=Luton_Points[6]+1
            if data["data"][i]["home_team"] == "Tottenham":
                Tottenham_Points[0]=Tottenham_Points[0]+1
                Tottenham_Points[1]=Tottenham_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Tottenham_Points[5]=Tottenham_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Tottenham_Points[6]=Tottenham_Points[6]+1
            if data["data"][i]["home_team"] == "Liverpool":
                Liverpool_Points[0]=Liverpool_Points[0]+1
                Liverpool_Points[1]=Liverpool_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Liverpool_Points[5]=Liverpool_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Liverpool_Points[6]=Liverpool_Points[6]+1
            if data["data"][i]["home_team"] == "Nottingham":
                Nottingham_Points[0]=Nottingham_Points[0]+1
                Nottingham_Points[1]=Nottingham_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Nottingham_Points[5]=Nottingham_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Nottingham_Points[6]=Nottingham_Points[6]+1
            if data["data"][i]["home_team"] == "Brentford":
                Brentford_Points[0]=Brentford_Points[0]+1
                Brentford_Points[1]=Brentford_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Brentford_Points[5]=Brentford_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Brentford_Points[6]=Brentford_Points[6]+1
            if data["data"][i]["home_team"] == "Fulham":
                Fulham_Points[0]=Fulham_Points[0]+1
                Fulham_Points[1]=Fulham_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Fulham_Points[5]=Fulham_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Fulham_Points[6]=Fulham_Points[6]+1
            if data["data"][i]["home_team"] == "Chelsea":
                Chelsea_Points[0]=Chelsea_Points[0]+1
                Chelsea_Points[1]=Chelsea_Points[1]+1
                if int(data["data"][i]["round "])>=last_round-4:
                     Chelsea_Points[5]=Chelsea_Points[5]+1
                if int(data["data"][i]["round "])>=last_round-9:
                     Chelsea_Points[6]=Chelsea_Points[6]+1
        ##Bramki strzelone/Bramki stracone
        if data["data"][i]["away_team"] == "Aston Villa":
                Aston_Villa_Points[3]=Aston_Villa_Points[3]+data["data"][i]["away_goals"]
                Aston_Villa_Points[4]=Aston_Villa_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Brighton":
                Brighton_Points[3]=Brighton_Points[3]+data["data"][i]["away_goals"]
                Brighton_Points[4]=Brighton_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Man United":
                Man_United_Points[3]=Man_United_Points[3]+data["data"][i]["away_goals"]
                Man_United_Points[4]=Man_United_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Crystal Palace":
                Crystal_Palace_Points[3]=Crystal_Palace_Points[3]+data["data"][i]["away_goals"]
                Crystal_Palace_Points[4]=Crystal_Palace_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Newcastle":
                Newcastle_Points[3]=Newcastle_Points[3]+data["data"][i]["away_goals"]
                Newcastle_Points[4]=Newcastle_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Burnley":
                Burnley_Points[3]=Burnley_Points[3]+data["data"][i]["away_goals"]
                Burnley_Points[4]=Burnley_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Wolves":
                Wolves_Points[3]=Wolves_Points[3]+data["data"][i]["away_goals"]
                Wolves_Points[4]=Wolves_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Man City":
                Man_City_Points[3]=Man_City_Points[3]+data["data"][i]["away_goals"]
                Man_City_Points[4]=Man_City_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Bournemouth":
                Bournemouth_Points[3]=Bournemouth_Points[3]+data["data"][i]["away_goals"]
                Bournemouth_Points[4]=Bournemouth_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Arsenal":
                Arsenal_Points[3]=Arsenal_Points[3]+data["data"][i]["away_goals"]
                Arsenal_Points[4]=Arsenal_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "West Ham":
                West_ham_Points[3]=West_ham_Points[3]+data["data"][i]["away_goals"]
                West_ham_Points[4]=West_ham_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Sheffield":
                Sheffield_Points[3]=Sheffield_Points[3]+data["data"][i]["away_goals"]
                Sheffield_Points[4]=Sheffield_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Everton":
                Everton_Points[3]=Everton_Points[3]+data["data"][i]["away_goals"]
                Everton_Points[4]=Everton_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Luton":
                Luton_Points[3]=Luton_Points[3]+data["data"][i]["away_goals"]
                Luton_Points[4]=Luton_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Tottenham":
                Tottenham_Points[3]=Tottenham_Points[3]+data["data"][i]["away_goals"]
                Tottenham_Points[4]=Tottenham_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Liverpool":
                Liverpool_Points[3]=Liverpool_Points[3]+data["data"][i]["away_goals"]
                Liverpool_Points[4]=Liverpool_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Nottingham":
                Nottingham_Points[3]=Nottingham_Points[3]+data["data"][i]["away_goals"]
                Nottingham_Points[4]=Nottingham_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Brentford":
                Brentford_Points[3]=Brentford_Points[3]+data["data"][i]["away_goals"]
                Brentford_Points[4]=Brentford_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Fulham":
                Fulham_Points[3]=Fulham_Points[3]+data["data"][i]["away_goals"]
                Fulham_Points[4]=Fulham_Points[4]+data["data"][i]["home_goals"]
        if data["data"][i]["away_team"] == "Chelsea":
                Chelsea_Points[3]=Chelsea_Points[3]+data["data"][i]["away_goals"] 
                Chelsea_Points[4]=Chelsea_Points[4]+data["data"][i]["home_goals"] 
        if data["data"][i]["home_team"] == "Aston Villa":
                Aston_Villa_Points[3]=Aston_Villa_Points[3]+data["data"][i]["home_goals"]
                Aston_Villa_Points[4]=Aston_Villa_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Brighton":
                Brighton_Points[3]=Brighton_Points[3]+data["data"][i]["home_goals"]
                Brighton_Points[4]=Brighton_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Man United":
                Man_United_Points[3]=Man_United_Points[3]+data["data"][i]["home_goals"]
                Man_United_Points[4]=Man_United_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Crystal Palace":
                Crystal_Palace_Points[3]=Crystal_Palace_Points[3]+data["data"][i]["home_goals"]
                Crystal_Palace_Points[4]=Crystal_Palace_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Newcastle":
                Newcastle_Points[3]=Newcastle_Points[3]+data["data"][i]["home_goals"]
                Newcastle_Points[4]=Newcastle_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Burnley":
                Burnley_Points[3]=Burnley_Points[3]+data["data"][i]["home_goals"]
                Burnley_Points[4]=Burnley_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Wolves":
                Wolves_Points[3]=Wolves_Points[3]+data["data"][i]["home_goals"]
                Wolves_Points[4]=Wolves_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Man City":
                Man_City_Points[3]=Man_City_Points[3]+data["data"][i]["home_goals"]
                Man_City_Points[4]=Man_City_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Bournemouth":
                Bournemouth_Points[3]=Bournemouth_Points[3]+data["data"][i]["home_goals"]
                Bournemouth_Points[4]=Bournemouth_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Arsenal":
                Arsenal_Points[3]=Arsenal_Points[3]+data["data"][i]["home_goals"]
                Arsenal_Points[4]=Arsenal_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "West Ham":
                West_ham_Points[3]=West_ham_Points[3]+data["data"][i]["home_goals"]
                West_ham_Points[4]=West_ham_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Sheffield":
                Sheffield_Points[3]=Sheffield_Points[3]+data["data"][i]["home_goals"]
                Sheffield_Points[4]=Sheffield_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Everton":
                Everton_Points[3]=Everton_Points[3]+data["data"][i]["home_goals"]
                Everton_Points[4]=Everton_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Luton":
                Luton_Points[3]=Luton_Points[3]+data["data"][i]["home_goals"]
                Luton_Points[4]=Luton_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Tottenham":
                Tottenham_Points[3]=Tottenham_Points[3]+data["data"][i]["home_goals"]
                Tottenham_Points[4]=Tottenham_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Liverpool":
                Liverpool_Points[3]=Liverpool_Points[3]+data["data"][i]["home_goals"]
                Liverpool_Points[4]=Liverpool_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Nottingham":
                Nottingham_Points[3]=Nottingham_Points[3]+data["data"][i]["home_goals"]
                Nottingham_Points[4]=Nottingham_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Brentford":
                Brentford_Points[3]=Brentford_Points[3]+data["data"][i]["home_goals"]
                Brentford_Points[4]=Brentford_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Fulham":
                Fulham_Points[3]=Fulham_Points[3]+data["data"][i]["home_goals"]
                Fulham_Points[4]=Fulham_Points[4]+data["data"][i]["away_goals"]
        if data["data"][i]["home_team"] == "Chelsea":
                Chelsea_Points[3]=Chelsea_Points[3]+data["data"][i]["home_goals"]
                Chelsea_Points[4]=Chelsea_Points[4]+data["data"][i]["away_goals"]
    
        
    
    def prediction(home, away):
         home_score=(home[0]*0.15)+(home[1]*0.1)+(home[3]*0.075)-(home[4]*0.075)+(home[5]*0.4)+(home[6]*0.2)
         away_score=(away[0]*0.15)+(away[2]*0.1)+(away[3]*0.075)-(away[4]*0.075)+(away[5]*0.4)+(away[6]*0.2)
         full_score=home_score+away_score
         home_chance=home_score/full_score
         away_chance=away_score/full_score
         print("home chance to win =", round(home_chance, 3), "away chance to win=", round(away_chance, 3))
    
    




