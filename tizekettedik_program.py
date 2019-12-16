import csv
import shapefile
from pyproj import Transformer

transformer = Transformer.from_crs("EPSG:4326", "EPSG:23700", always_xy=True)

csv_file = open("pois2.csv", "r", encoding="ISO 8859-2")
csv_reader = csv.DictReader(csv_file, delimiter=";")

shp_writer = shapefile.Writer("line", shapeType=3)
shp_writer.field('seq', "N")

line = []
prev_seq = 1

for idx, row in enumerate(csv_reader):
    
    coord_x = float(row['X'])
    coord_y = float(row['Y'])

    coord = [coord_x, coord_y]
    
    if epsgCode == 23700:
        coord = transformer.transform(coord_x, coord_y)

    print(coord)
    
    seq = int(row['seq'])

    if prev_seq != seq:
        print(seq, prev_seq)
        shp_writer.record(seq=prev_seq)
        shp_writer.line([line])

        line = []
        line.append(coord)
    
    else:

        line.append(coord)
    
    prev_seq = seq

shp_writer.record(seq=prev_seq)
shp_writer.line([line])

shp_writer.close()
csv_file.close()
