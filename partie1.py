import pandas as pd
from matplotlib import pyplot as plt

#Pays : Italy Spain France US Norway Equador Japan Régions : Hubei Henan

tab = [62, 60, 137, 202, 116, 226, 179, 97, 139]

dataConfirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')
dataDeaths = pd.read_csv('time_series_covid19_deaths_global.csv')

fig, axs = plt.subplots(2, 1, constrained_layout=True)

regions_name = []
confirmed_value = []
death_value = []

for id in tab :
    region = ""
    if (str(dataConfirmed.loc[id, 'Province/State']) != "nan"):
        region = '(' + str(dataConfirmed.loc[id, 'Province/State']) + ')'
    legend = str(dataConfirmed.loc[id, "Country/Region"]) + region
    regions_name.append(legend)
    death_value.append(dataDeaths.loc[id, "3/22/20"])
    confirmed_value.append(dataConfirmed.loc[id, "3/22/20"])

    print("In "+ str(legend) + " :")
    print("Confirmed cases : ")
    print(dataConfirmed.loc[id, "3/22/20"])
    print("Deaths : ")
    print(dataDeaths.loc[id, "3/22/20"])
    print()

axs[0].bar(regions_name, death_value)
axs[0].set_title('Nombre de Mort du COVID-19')
axs[1].bar(regions_name, confirmed_value)
axs[1].set_title('Nombre de cas confirmés du COVID-19')
plt.show()