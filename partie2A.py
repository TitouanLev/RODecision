import pandas as pd
from matplotlib import pyplot as plt

tab = [62, 60, 137, 202, 116, 226, 179, 97, 139]

dataConfirmed = pd.read_csv('time_series_covid19_confirmed_global.csv').loc[tab]
dataDeaths = pd.read_csv('time_series_covid19_deaths_global.csv').loc[tab]

dates = list(dataConfirmed.columns.values)[4:]

for index, row in dataConfirmed.iterrows():
    values = []
    for d in dates:
        values.append(row[d])
    plt.title("Nombre de cas confirmé")
    region = ""
    if (str(row['Province/State']) != "nan") :
        region = '(' + str(row['Province/State']) + ')'
    legend = str(row["Country/Region"]) + region
    plt.plot(dates, values, label=legend)
    plt.legend(loc="upper left")
    plt.xticks(rotation=45)


plt.show()
