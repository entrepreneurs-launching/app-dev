#!/usr/local/bin/python3
import json
import requests
import importlib

connappsync = importlib.import_module('aws-appsync-session')
attrqueries = importlib.import_module('aws-appsync-attr-queries')
tripadvisorjson = importlib.import_module('Attractions-json')


def insertAttrItem(fields):
    query = attrqueries.query1
    variables = {
        'id': fields[0],
        'json': fields[1],
        'weburl': fields[2],
        'lat': fields[3],
        'lon': fields[4],
        'pluscode': fields[5],
        'name': fields[6],
        'city': fields[7],
        'state': fields[8],
        'description': fields[9],
        'address': fields[10],
        'ranking': fields[11],
        'rating': fields[12],
        'numrev': fields[13],
        'numphoto': fields[14],
        'category1': fields[15],
        'category2': fields[16],
        'category3': fields[17],
        'category4': fields[18],
        'category5': fields[19],
        'category6': fields[20],
        'category7': fields[21],
        'category8': fields[22],
        'category9': fields[23]
    }
    response = connappsync.sendRequest(json={
        'query': query,
        'variables': variables
    })
    if 'errors' in str(response.text):
        print (response.text)
        print ('aws request failed for location:', fields[0])
    else:
        awsjson = json.loads(response.text)['data']['createAttractions']
        if awsjson['id']    == fields[0] and awsjson['name'] == fields[6]:
           print('location', fields[0], 'SUCCESSFULLY SAVED to AWS Appsync')


def savetoamplify(unformattedjson):
    fields = tripadvisorjson.parsefields(unformattedjson)
    ret = insertAttrItem(fields)


"""
response = requests.get(
    'https://api.content.tripadvisor.com/api/v1/location/7261633/details?language=en&key=07D72A1029CF4CA08200D3A8261DF2B2'
)
assert response.status_code == 200, 'sup:2 trip advisor locaiton details api request failed' + str(
    response.status_code)
unformattedjson = json.loads(response.text)
parsefields(unformattedjson)
"""