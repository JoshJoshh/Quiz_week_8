import matplotlib.pyplot as plt
import pandas as pd

years = []
co2 = []
temp = []
file = pd.read_csv('climate.csv')
for a in range(len(file.values)):
    years.append(file.values[a][0])
    co2.append(file.values[a][1])
    temp.append(file.values[a][2])

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
plt.savefig("co2_temp_2.png") 

