pois_csv = open("pois.csv", "r", encoding="UTF-8")

pois = pois_csv.read()
pois_line = pois.splitlines()

data = []

for line in pois_line:

    fields = line.split(',')
    data.append(fields)

print(data[0][5])

pois_csv.close()