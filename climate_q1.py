import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

years = []
co2 = []
temp = []
file = sqlite3.connect('climate.db')
for a in range(len(pd.read_sql_query("SELECT * FROM ClimateData",file).values)):
    years.append(pd.read_sql_query("SELECT Year FROM ClimateData",file).values[a][0])
    co2.append(pd.read_sql_query("SELECT CO2 FROM ClimateData",file).values[a][0])
    temp.append(pd.read_sql_query("SELECT Temperature FROM ClimateData",file).values[a][0])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")
