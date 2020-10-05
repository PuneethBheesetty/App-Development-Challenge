#https://docs.python.org/3/library/csv.html
import csv
with open ("fy20_adc_data_file_88_degrees.csv", newline="") as csvfile:
	for row in cvs.reader(csvfile, delimiter=","):
		print row;
