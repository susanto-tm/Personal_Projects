import matplotlib.pyplot as plt
import csv

x = []
y = []

with open("summary.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        x.append(int(row[0]))
        y.append(float(row[1]))

plt.plot(x, y, label="Trend")
plt.xlabel("Year")
plt.ylabel("TCMC Used")
plt.title("Summary")
plt.legend()
plt.show()

