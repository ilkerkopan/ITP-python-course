import matplotlib.pyplot as plt
import csv

temperature = []
temperature_smooth = []
with open("C:/Users/ilker/Documents/weather.csv") as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        temperature.append(float(row[1]))

temperature_smooth.append(temperature[0])
for i in range(1,len(temperature)-1):
    temperature_smooth.append((temperature[i-1] + temperature[i] + temperature[i+1])/3)

temperature_smooth.append(temperature[-1])
plt.plot(temperature, label='original')
plt.plot(temperature_smooth, label='smooth', c='red')
plt.title("Weather Data Points", fontsize=24)
plt.xlabel("Data point number", fontsize=14)
plt.ylabel("Temperature Celcius", fontsize=14)
plt.legend()
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
plt.show()