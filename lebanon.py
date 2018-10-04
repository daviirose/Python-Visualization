import matplotlib.pyplot as plt
import numpy as np
import csv

results = []
dates = []
values = []

with open("lebanon.csv") as csvfile:
    reader = csv.reader(csvfile)
    #next(reader, None)
    for row in reader:

        dates.append(row[1])
        values.append(row[2])
plt.bar(dates, values)
plt.xticks(rotation=45)
plt.show()