import csv
import argparse

parser = argparse.ArgumentParser(description="CSV író program")

parser.add_argument('--out', help="A létrehozott file helye és neve")

args = parser.parse_args()
outfile = args.out
boltok = [
    {'x': 17, 'y': 47, 'id': 'A1', 'open': True},
    {'x': 18, 'y': 48, 'id': 'A2', 'open': True},
    {'x': 19, 'y': 49, 'id': 'B1', 'open': False}
]

fieldnames = list(boltok[0])
print(fieldnames)
file = open(outfile, "w", encoding="UTF-8", newline='')

csv_writer = csv.DictWriter(file, delimiter=";", fieldnames=fieldnames)

csv_writer.writeheader()
csv_writer.writerows(boltok)

file.close()