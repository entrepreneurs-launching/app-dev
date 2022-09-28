#!/usr/local/bin/python3


def findall(v, k, retarray):
    if type(v) == type({}):
        for k1 in v:
            if k1 == k:
                # print (v[k1])
                retarray.append(v[k1])
            findall(v[k1], k, retarray)
    if type(v) == type([]):
        for el in v:
            findall(el, k, retarray)


def gettrycatch(json, key1, key2=None, key3=None):
    value = ""
    try:
        if key3:
            value = json[key1][key2][key3]
        elif key2:
            value = json[key1][key2]
        elif key1:
            value = json[key1]
    except:
        print('could not find', key1, key2, key3, 'in json')
    return value


def parsefields(unformattedjson):
    id = gettrycatch(unformattedjson, 'location_id')
    json = unformattedjson
    weburl = gettrycatch(unformattedjson, 'web_url')
    lat = gettrycatch(unformattedjson, 'latitude')
    lon = gettrycatch(unformattedjson, 'longitude')
    pluscode = ""
    name = gettrycatch(unformattedjson, 'name')
    city = gettrycatch(unformattedjson, 'address_obj', 'city')
    state = gettrycatch(unformattedjson, 'address_obj', 'state')
    desc = ""
    address = gettrycatch(unformattedjson, 'address_obj', 'address_string')
    ranking = gettrycatch(unformattedjson, 'ranking_data', 'ranking')
    rating = gettrycatch(unformattedjson, 'rating')
    numrev = gettrycatch(unformattedjson, 'num_reviews')
    numphoto = gettrycatch(unformattedjson, 'photo_count')

    catarray = []
    findall(unformattedjson, 'localized_name', catarray)
    catarray += [""] * 10

    category1 = catarray[0]
    category2 = catarray[1]
    category3 = catarray[2]
    category4 = catarray[3]
    category5 = catarray[4]
    category6 = catarray[5]
    category7 = catarray[6]
    category8 = catarray[7]
    category9 = catarray[8]

    # print (id, unformattedjson[:10], weburl[:20], address)
    # print(id, lat, lon, name, city, state, address)
    # print(ranking, rating, numrev, numphoto)
    # print(catarray, len(catarray))

    return [
        id, json, weburl, lat, lon, pluscode, name, city, state, desc,
        address, ranking, rating, numrev, numphoto, category1, category2,
        category3, category4, category5, category6, category7, category8,
        category9
    ]
