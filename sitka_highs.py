from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


with open('/Users/linruyi/Desktop/the_csv_file_format/weather_data/sitka_weather_2021_simple.csv','r') as f:

    lines = csv.reader(f)

# names = ["jane","jessy","spring"]
    temp = []
    i=1
    for line in lines:
        
        if i == 1:
            i+=1
            continue
        # print(line)
        # print(line[5])

        # linelist = line.split(",")
        # print(linelist)
        # for high in linelist[0:]:
            # print(high)
            # Temp = high.split(",")
            # for t in Temp:
                # print(t)
            # temp=[]
        temp.append(int(line[5]))
        # print(temp)
    print(temp)

    fig, ax = plt.subplots()

    ax.plot(temp[0:], color='red')
    plt.yticks(range(0,60,20))
    ax.set_title("Daily High Temperatures, 2021", fontsize=24)
    ax.set_xlabel('day', fontsize=16)
    ax.set_ylabel('Temp', fontsize=16)
    plt.show()

# # Extract dates and high temperatures.
# dates, highs = [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], '%Y-%m-%d')
#     high = int(row[4])
#     dates.append(current_date)
#     highs.append(high)

# # Plot the high temperatures.
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, color='red')

# # Format plot.
# ax.set_title("Daily High Temperatures, 2021", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(labelsize=16)