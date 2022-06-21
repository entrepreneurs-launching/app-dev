#!/usr/local/bin/python3

import os
import json
import urllib
import requests

"""
https://serpapi.com/search.json?engine=google&q=badami+karnataka+beautiful&google_domain=google.co.in&gl=in&hl=en&tbm=isch&api_key=b337b4f036aaede4f708046b6338cf100481d6247ffe7d9b3ad472d2e8667d49
https://serpapi.com/search.json?engine=google&q=badami%2Bkarnataka%2Bbeautiful&google_domain=google.co.in&gl=in&hl=en&tbm=isch&api_key=b337b4f036aaede4f708046b6338cf100481d6247ffe7d9b3ad472d2e8667d49
"""
serpapiurl = 'https://serpapi.com/search.json?'
saltstring = ['beautiful', 'gorgeous', 'exotic', 'picturesque']


def deleteImages(imagearray):
    pass

def saveImage(imageurl, imagearray):
    response = requests.get(imageurl)
    assert response.status_code == 200, 'sup: image download failed from serpapi url'

    imagefilename = os.path.basename(imageurl)
    if response.status_code == 200:
        with open(imagefilename, 'wb') as f:
            f.write(response.content)

    imagearray.append((imagefilename, os.path.getsize(imagefilename)))


def getJSON(querystring, imagearray):
    print ('sup: image search: ', querystring)
    
    # querystring = 'badami+karnataka+beautiful'

    url = serpapiurl
    params = {
        'engine': 'google',
        'q': querystring,
        'google_domain': 'google.co.in',
        'gl': 'in',
        'hl': 'en',
        'tbm': 'isch',
        'api_key': 'b337b4f036aaede4f708046b6338cf100481d6247ffe7d9b3ad472d2e8667d49',
    }
    req = url + urllib.parse.urlencode(params)
    # print(req)

    res = requests.get(req)
    # print (res.status_code)
    assert res.status_code, 200
    # print (res.text)

    response = json.loads(res.text)
    assert response['search_metadata']['status'] == 'Success'

    resultsarray = response['images_results']
    # print (resultsarray)
    thiscount = len(resultsarray)

    for i in range(min(10, thiscount)):
        print(resultsarray[i]['thumbnail'])
        saveImage(resultsarray[i]['thumbnail'], imagearray)


def getImages(querystring, imagearray):
    print ('sup: image search: ', querystring)
    getJSON(querystring + ' ' + saltstring[0], imagearray)


"""
imagearray = []
getJSON('abcd', imagearray)
print (imagearray)
"""