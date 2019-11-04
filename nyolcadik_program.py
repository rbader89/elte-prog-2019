import csv
import argparse

parser = argparse.ArgumentParser(description="POI olvasó program")
parser.add_argument('--infile', help="Bemeneti file elérési útja")

args = parser.parse_args()

pois_csv = open(args.infile, "r", encoding="UTF-8")

# csv_file = csv.reader(pois_csv, delimiter=',')

# for line in csv_file:

#     print(line[1])

csv_file_dict = csv.DictReader(pois_csv, delimiter=",")
print(csv_file_dict)
print(csv_file_dict.fieldnames)

for line in csv_file_dict:

    print(line['osm_id'])