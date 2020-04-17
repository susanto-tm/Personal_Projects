import glob, csv

# header TCMC
# plot against x = time, y = # card swiped

files = []

for file in glob.glob("./MetroData/*.csv"):
    files.append(file.split("\\")[-1])

summary = []

year = 2009
count = 0
total = 0

for file in files:
    if count % 2 == 0:
        year += 1
    with open("./MetroData/" + file, 'r') as f:
        reader = csv.reader(f)
        for row in list(reader)[3:]:
            total += float(row[13])

    if (count + 1) % 2 == 0:
        summary.append([year, total])
        total = 0

    count += 1

with open("summary.csv", 'w') as f:
    for year in summary:
        f.write(f'{year[0]},{year[1]}\n')
