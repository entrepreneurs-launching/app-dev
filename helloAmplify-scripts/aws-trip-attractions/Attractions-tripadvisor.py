#!/usr/local/bin/python3

import json
import requests

radiuskm = 10
tripadvisorkey = "07D72A1029CF4CA08200D3A8261DF2B2"

tripadvisordailylimit = 9990
tripadvisorapicountfile = 'tripadvisor-apicount.noedit'


def checkapilimitpause():
    apicount = 0

    # read api count
    with open(tripadvisorapicountfile, 'r') as f:
        apicount = int(f.readline())
        f.close()

    print ('Tripadvisor current api count:', apicount)
    apicount += 1

    # check and pause and reset
    if apicount > tripadvisordailylimit:
        print ('Tripadvisor API Limit reached. waiting 24 hours')
        time.sleep(86400)
        apicount = 0

    # write api count
    with open(tripadvisorapicountfile, 'w') as f:
        f.writelines([str(apicount)])
        f.close()


nearbyendpointstr = "https://api.content.tripadvisor.com/api/v1/location/nearby_search"
keystr = "key=" + tripadvisorkey
radiusstr = "radius=" + str(radiuskm)
categorystr = "category=attractions"
radiusUnitstr = "radiusUnit=km"
languagestr = "language=en"

locationendpointstr = "https://api.content.tripadvisor.com/api/v1/location"
"""
https://api.content.tripadvisor.com/api/v1/location/nearby_search?latLong=22.549911771084783%2C%2088.35155141547888&category=attractions&radius=10&radiusUnit=km&language=en&key=07D72A1029CF4CA08200D3A8261DF2B2
"""


def islocationAttraction(locationdetailsjson):
    # print (locationdetailsjson)
    if 'attraction' in str(locationdetailsjson):
        return True
    if 'Attraction' in str(locationdetailsjson):
        return True
    return False


def getlocationdetails(locationid):
    locationidstr = str(locationid)
    locationdetailsstr = locationendpointstr + "/" + locationidstr + "/" + "details" + "?" + languagestr + "&" + keystr
    print(locationdetailsstr)

    checkapilimitpause()
    response = requests.get(locationdetailsstr)
    assert response.status_code == 200, 'sup:2 trip advisor locaiton details api request failed' + str(
        response.status_code)
    # print (response.text)

    unformattedjson = json.loads(response.text)
    return unformattedjson


def getnearbyjson(lat, lon):
    latlongstr = "latLong=" + str(lat) + "," + str(lon)
    nearbyurl = nearbyendpointstr + "?" + latlongstr + "&" + categorystr + "&" + radiusstr + "&" + radiusUnitstr + "&" + languagestr + "&" + keystr
    print(nearbyurl)

    checkapilimitpause()
    response = requests.get(nearbyurl)
    assert response.status_code == 200, 'sup:1 trip advisor nearby api request failed' + str(
        response.status_code)
    # print (response.text)

    unformattedjson = json.loads(response.text)
    return unformattedjson


# getnearbyjson(15.7129, 74.3354) # returns 2  locations
# getnearbyjson(13.1438, 77.6169) # returns 10 locations
