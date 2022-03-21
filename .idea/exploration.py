import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import math

df = pd.read_csv('datasources/ten_up.csv', parse_dates=True)
df['DISCOVERY_DATE'] = pd.to_datetime(df['DISCOVERY_DATE'], errors ='coerce')
df['CONT_DATE'] = pd.to_datetime(df['CONT_DATE'], errors ='coerce')

x = df['LONGITUDE']
y = df['LATITUDE']
size = df['FIRE_SIZE']

x_data = []
y_data = []
size_data = []

i = datetime.date(month = 12, day=31, year=2013)
a = datetime.date(month  = 1, day = 1, year=2012)
while a <= i:
    for value in range(df.shape[0]):
        if df['DISCOVERY_DATE'][value] <= a:
            if df['CONT_DATE'][value] >= a:
                x_data.append(x[value])
                y_data.append(y[value])
                size_data.append((size[value]/50)+1)

    a += datetime.timedelta(days=1)
    print(a)
    plt.clf()
    plt.xlim(-109, -102)
    plt.ylim(37, 41)
    plt.xlabel(a)
    plt.scatter(x_data, y_data, color='red', s = size_data)
    plt.pause(0.001)

    x_data = []
    y_data = []
    size_data = []

plt.show()

