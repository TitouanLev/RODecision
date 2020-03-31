import pandas as pd

#Pays : Italy Spain France US Norway Equador Japan Ville : Hubei Henan

zones = ["Italy", "Spain", "France", "US", "Norway", "Equador", "Japan"]
villes = ["Hubei", "Henan"]

dataConfirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')
dataDeaths = pd.read_csv('time_series_covid19_deaths_global.csv')

for z in villes :
    print("In "+z + " :")
    print("Confirmed cases : ")
    print(dataConfirmed[dataConfirmed['Province/State'] == z])
    print("Deaths : ")
    print(dataDeaths[dataDeaths["Province/State"] == z])
    print()

for z in zones :
    print("In "+z + " :")
    print("Confirmed cases : ")
    print(dataConfirmed[dataConfirmed['Country/Region'] == z])
    print("Deaths : ")
    print(dataDeaths[dataDeaths["Country/Region"] == z])
    print()