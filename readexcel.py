#https://docs.python.org/3/library/csv.html
import csv
with open ("fy20_adc_data_file_88_degrees.csv", newline="") as csvfile:
	for row in csv.reader(csvfile, delimiter=","):
		latitude = row[0];
		longitude = row[1];
		height = row[2];
		slope = row[3];
