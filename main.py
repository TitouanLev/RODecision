import pandas as pd
from matplotlib import pyplot as plt

dataConfirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')

plt.plot(dataConfirmed["Country/Region"], dataConfirmed["3/22/20"])

plt.show()