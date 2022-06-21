#!/usr/local/bin/python3

from openpyxl import load_workbook

filename = "Trips.xlsx"
#load excel file
workbook = load_workbook(filename=filename)
 
#open workbook
sheet = workbook.active




# hardcode dst column names
_id="A"
_code = "B"
_lat = "C"
_lon = "D"
_latlon = "E"
_place = "F"
_state = "G"
_image = "H"
_months = "I"
_category = "J"
_mindays = "K"
_maxdays = "L"
_description = "M"


for i in range(2, 30):

	row = str(i)
	cell = _place+row	
	srcvalue = sheet[cell].value
	if srcvalue == None:
		break

	srcvalue = srcvalue.split(',')
	if len(srcvalue) > 0:
		place = srcvalue[0].strip()
	if len(srcvalue) > 1:
		state = srcvalue[1].strip()
	
	dstcell = _place+row
	sheet[dstcell] = place
	dstcell = _state+row
	sheet[dstcell] = state



#save the file
workbook.save(filename=filename)
