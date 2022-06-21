#!/usr/local/bin/python3

import json
import time
import boto3
import requests
from requests_aws4auth import AWS4Auth
import importlib
import logging
import datetime


# Config
# Only process record where id == code. If id code mismatch, treat it as a trash record and skip it
idcodecheck = True
updatenullimageonly = True


logging.basicConfig(filename=str(datetime.datetime.now()) + '.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.info("Starting image update script")
logger = logging.getLogger('aws-appsync')
logger.info("Starting image update script 2")
logger = logging.getLogger('aws-s3')
logger.info("Starting image update script 3")

connappsync = importlib.import_module('aws-appsync-session')
tripqueries = importlib.import_module('aws-appsync-trip-queries')
serpqueries = importlib.import_module('serpapi-google-image')
awss3bucket = importlib.import_module('aws-s3-bucket-upload-download')

#################################### Functions ##################################






def getTripItem(id):
    query = tripqueries.query2
    variables = {'id': id}
    response = connappsync.sendRequest(
        json={'query': query, 'variables': variables}
    )
    print(response.text)
    response = json.loads(response.text)
    return response


def updateTripItem(id, imagerecord):
    query = tripqueries.query3
    variables = {'id': id, 'image': imagerecord}
    response = connappsync.sendRequest(
        json={'query': query, 'variables': variables}
    )
    print(response.text)
    response = json.loads(response.text)
    return response


def processTripList():
    limit = 5
    query = tripqueries.query1
    variables = {'limit': limit}

    nextToken = 0
    itemcount = 0

    while nextToken != None:
        print('sup: send GraphQL API request')

        # Post the request...
        response = connappsync.sendRequest(
            json={'query': query, 'variables': variables}
        )
        # print (response.text)

        response = json.loads(response.text)
        # print (json.dumps(response, indent=4))
        # print (response['data']['listTrips']['nextToken'])

        nextToken = response['data']['listTrips']['nextToken']
        thiscount = len(response['data']['listTrips']['items'])
        itemcount += thiscount
        # print (thiscount, 'items total: ', itemcount, 'items')

        for i in range(thiscount):
            item  = response['data']['listTrips']['items'][i]
            id    = item['id']
            code  = item['code']
            place = item['place']
            state = item['state']
            image = item['image']
            
            print('sup: process item:', id, code, place, image)
            processTripItem(code, place, state, item)

            item = id = code = place = image = None
        thiscount = 0

        query = tripqueries.queryn
        variables = {'limit': limit, 'nextToken': nextToken}
        time.sleep(1)


def processTripItem(code, place=None, state=None, item=None):
    if place == None or state == None:
        response = getTripItem(code)
        item  = response['data']['getTrips']
        id    = item['id']
        code  = item['code']
        place = item['place']
        state = item['state']
        image = item['image']
        if place == None or state == None or item == None:
            return

        print('sup: process item:', id, code, place, image)
        processTripItem(code, place, state, item)
        return


    id    = item['id']
    code  = item['code']
    place = item['place']
    state = item['state']
    image = item['image']
    
    # sup:config
    if idcodecheck and id != code:  # not a valid entry, skip or fix manually
        return
    if updatenullimageonly and image:
        print('sup: image already installed. skip:', code, image)
        return
    

    #### CALL SERPAPI ####
    imagearray = []
    serpqueries.getImages(place + ' ' + state, imagearray)
    # print (imagearray)
    # CALLS INTO S3 AND AWS MUTATION TO UPDATE IMAGE
    installImagesAWS(code, imagearray)
    serpqueries.deleteImages(imagearray)


def installImagesAWS(code, imagearray):
    imagerecord = ""

    # copy images into s3 with proper names
    l = len(imagearray)
    for i in range(l):
        
        localefile = imagearray[i][0]
        remotefile = 'img-'+code+'-'+str(i)+'.jpeg'
        print ('sup: uploading to s3: file: ', localefile, 'to', remotefile)
        ret = awss3bucket.upload_file(awss3bucket.bucket_name, localefile, remotefile)
        if ret == False:
            print ('sup: image upload failed code: ', code, 'image file: ', localefile, remotefile)
        else:
            imagerecord += remotefile + ', '

    # convert image array into the record format. it should be a s3 url
    print ('sup:', imagerecord)

    # send updateMutation with that record
    # validate the updateMutation response with the sent values
    response = updateTripItem(code, imagerecord)
    item  = response['data']['updateTrips']
    id    = item['id']
    code  = item['code']
    place = item['place']
    state = item['state']
    image = item['image']
    pass
    

    

#################################### Calls ##################################


processTripList()
# processTripItem('7J5V9MCH+8V')
