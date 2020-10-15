#https://docs.python.org/3/library/csv.html
import csv
import bpy
with open ("fy20_adc_data_file_88_degrees.csv", newline="") as lunar_data:
	for row in csv.reader(lunar_data):
		latitude = row[0];
		longitude = row[1];
		height = row[2];
		slope = row[3];
		bpy.ops.mesh.primitive_point.add[location={latitude, longitude, height}]
