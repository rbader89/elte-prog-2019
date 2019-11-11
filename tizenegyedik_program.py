import csv
import shapefile

csv_file = open("pois.csv", "r", encoding="UTF8")
csv_reader = csv.reader(csv_file, delimiter=",")

shp_writer = shapefile.Writer("pois", shapeType=1)

#X,Y,osm_id,code,fclass,name,x,y
shp_writer.field('X', fieldType='N')
shp_writer.field('Y', fieldType='N')
shp_writer.field('osm_id', fieldType='N')
shp_writer.field('code', fieldType='C')
shp_writer.field('fclass', fieldType='C')
shp_writer.field('name', fieldType='C')

for idx, row in enumerate(csv_reader):
    
    if idx != 0:
        shp_writer.point(float(row[0]), float(row[1]))
        shp_writer.record(X=float(row[0]), Y=float(row[1]), osm_id=int(row[2]),
        code=row[3], fclass=row[4], name=row[5])