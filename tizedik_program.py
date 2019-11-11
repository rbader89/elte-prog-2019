import shapefile
import csv

'''
PYSHAP doc: https://pypi.org/project/pyshp/#description
'''

shpfile = shapefile.Reader("disctricts.shp")
csvfile = open("disctricts.csv", 'w', encoding="UTF8", newline='')

csv_writer = csv.writer(csvfile, delimiter=";")

print(shpfile)

fields = shpfile.fields

csv_fields = []

for field in fields:

    if field[0] != 'DeletionFlag':

        csv_fields.append(field[0])

csv_writer.writerow(csv_fields)

rows = shpfile.records()

for row in rows:

    csv_writer.writerow(row)

csvfile.close()
