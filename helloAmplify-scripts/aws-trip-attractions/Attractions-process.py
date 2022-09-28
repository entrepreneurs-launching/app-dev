#!/usr/local/bin/python3

import os
import importlib
from openpyxl import load_workbook

tripadvisorapi = importlib.import_module('Attractions-tripadvisor')
awsappsyncapi = importlib.import_module('Attractions-aws')

filename = "Attractions.xlsx"
# load excel file
workbook = load_workbook(filename=filename)

# open workbook
sheet = workbook.active

# hardcode dst column names
_countrycode = "A"
_pincode = "B"
_street = "C"
_state = "D"
_statenumber = "E"
_distt = "F"
_unused1 = "G"
_city = "H"
_unused2 = "I"
_lat = "J"
_lon = "K"

# Open Attractions.xlsx, find the start and end line you wanna process
# Put the start row number in rowstart.txt
# Put the end   row number in rowend.txt

filecurr = 'rowcurr.noedit'
filestart = 'rowstart.txt'
fileend = 'rowend.txt'
fs = os.path.getmtime(filestart)
fc = os.path.getmtime(filecurr)
fe = os.path.getmtime(fileend)

if fc > fs and fc > fe:
    # continue from where we left off
    with open(filecurr, 'r') as f:
        rowcurr = int(f.readline())
        f.close()
    with open(fileend, 'r') as f:
        rowend = int(f.readline())
        f.close()

    rowstart = rowcurr + 1
    if rowstart > rowend:
        rowstart, rowend = rowend, rowstart
else:
    # we have new row numbers. start from beginning
    with open(filestart, 'r') as f:
        rowstart = int(f.readline())
        f.close()
    with open(fileend, 'r') as f:
        rowend = int(f.readline())
        f.close()

    if rowstart > rowend:
        rowstart, rowend = rowend, rowstart

print('reading', filename, 'row', rowstart, 'to', rowend)

for i in range(rowstart, rowend + 1):
    row = str(i)
    print(row)

    cell = _pincode + row
    pincode = sheet[cell].value

    cell = _lat + row
    lat = sheet[cell].value

    cell = _lon + row
    lon = sheet[cell].value

    cell = _distt + row
    distt = sheet[cell].value

    cell = _city + row
    city = sheet[cell].value

    print(i, " : ", pincode, lat, lon, distt, city)

    unformattedjson = tripadvisorapi.getnearbyjson(lat, lon)

    arrayofplaces = unformattedjson['data']
    countofplaces = len(arrayofplaces)
    # print (arrayofplaces)
    print("found", str(countofplaces), "places")

    for i in range(countofplaces):
        locationjson = arrayofplaces[i]
        locationid = locationjson['location_id']
        unformattedjson = tripadvisorapi.getlocationdetails(locationid)

        if tripadvisorapi.islocationAttraction(unformattedjson):
            print('This is an Attraction. SAVE')
            awsappsyncapi.savetoamplify(unformattedjson)
        else:
            print('This is NOT an Attraction')

    # save the current row in rowcurr.txt
    with open(filecurr, 'w') as f:
        f.writelines([str(row)])
        f.close()


# save the file
# workbook.save(filename=filename)
