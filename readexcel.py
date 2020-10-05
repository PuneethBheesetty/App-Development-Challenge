#https://openpyxl.readthedocs.io/en/stable/tutorial.html
from openpyxl import Workbook
wb = Workbook;
ws = wb.active;					#get the active worksheet
for row in ws.rows:			#select one row at a time
	latitude = row[0];
	longitude = row[1];
	height = row[2];
	slope = row[3];
	
