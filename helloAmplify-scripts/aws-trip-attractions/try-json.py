#!/usr/local/bin/python3

import re
import json


def find_values(id, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict)  # Return value ignored.
    return results


"""
json_repr = "{'location_id': '20048279', 'name': 'Taxi2Airport Bangalore', 'description': 'Taxi2Airport.com is an online reservation and booking system for airport transfers all around the globe. We are committed to providing safe and reliable transfers over all areas to and from all airports, cruise ports, and main train stations. Our service operates across 150+ countries and 1500+ airports with an excellent customer satisfaction rating of 4.5 out of 5 based on 35k+ reviews.', 'web_url': 'https://www.tripadvisor.com/Attraction_Review-g297628-d20048279-Reviews-Taxi2Airport_Bangalore-Bengaluru_Bangalore_District_Karnataka.html?m=66827', 'address_obj': {'street1': 'Weteringschans 28', 'city': 'Bengaluru', 'state': 'Karnataka', 'country': 'India', 'postalcode': '1017 SG', 'address_string': 'Weteringschans 28, Bengaluru 1017 SG India'}, 'ancestors': [{'level': 'City', 'name': 'Bengaluru', 'location_id': '297628'}, {'level': 'District', 'name': 'Bangalore District', 'location_id': '12392950'}, {'level': 'State', 'name': 'Karnataka', 'location_id': '297627'}, {'level': 'Country', 'name': 'India', 'location_id': '293860'}], 'latitude': '12.98987', 'longitude': '77.59281', 'timezone': 'Asia/Kolkata', 'email': 'support@taxi2airport.com', 'phone': '+31 88 318 8344', 'website': 'https://www.taxi2airport.com', 'write_review': 'https://www.tripadvisor.com/UserReview-g297628-d20048279-Taxi2Airport_Bangalore-Bengaluru_Bangalore_District_Karnataka.html?m=66827', 'num_reviews': '0', 'photo_count': '23', 'see_all_photos': 'https://www.tripadvisor.com/Attraction_Review-g297628-d20048279-m66827-Reviews-Taxi2Airport_Bangalore-Bengaluru_Bangalore_District_Karnataka.html#photos', 'category': {'name': 'attraction', 'localized_name': 'Attraction'}, 'subcategory': [{'name': 'transportation', 'localized_name': 'Transportation'}, {'name': 'other', 'localized_name': 'Other'}, {'name': 'attractions', 'localized_name': 'Attractions'}], 'groups': [{'name': 'Other', 'localized_name': 'Other', 'categories': [{'name': '', 'localized_name': ''}]}, {'name': 'Transportation', 'localized_name': 'Transportation', 'categories': [{'name': 'Taxis & Shuttles', 'localized_name': 'Taxis & Shuttles'}]}], 'neighborhood_info': [], 'trip_types': [{'name': 'business', 'localized_name': 'Business', 'value': '0'}, {'name': 'couples', 'localized_name': 'Couples', 'value': '0'}, {'name': 'solo', 'localized_name': 'Solo travel', 'value': '0'}, {'name': 'family', 'localized_name': 'Family', 'value': '0'}, {'name': 'friends', 'localized_name': 'Friends getaway', 'value': '0'}], 'awards': []}"
print(find_values('localized_name', json_repr))
"""


def deep_search(needles, haystack):
    found = {}
    if type(needles) != type([]):
        needles = [needles]

    if type(haystack) == type(dict()):
        for needle in needles:
            if needle in haystack.keys():
                found[needle] = haystack[needle]
            elif len(haystack.keys()) > 0:
                for key in haystack.keys():
                    result = deep_search(needle, haystack[key])
                    if result:
                        for k, v in result.items():
                            found[k] = v
    elif type(haystack) == type([]):
        for node in haystack:
            result = deep_search(needles, node)
            if result:
                for k, v in result.items():
                    found[k] = v
    return found


"""
json_string = "{'location_id': '20048279', 'name': 'Taxi2Airport Bangalore', 'description': 'Taxi2Airport.com is an online reservation and booking system for airport transfers all around the globe. We are committed to providing safe and reliable transfers over all areas to and from all airports, cruise ports, and main train stations. Our service operates across 150+ countries and 1500+ airports with an excellent customer satisfaction rating of 4.5 out of 5 based on 35k+ reviews.', 'web_url': 'https://www.tripadvisor.com/Attraction_Review-g297628-d20048279-Reviews-Taxi2Airport_Bangalore-Bengaluru_Bangalore_District_Karnataka.html?m=66827', 'address_obj': {'street1': 'Weteringschans 28', 'city': 'Bengaluru', 'state': 'Karnataka', 'country': 'India', 'postalcode': '1017 SG', 'address_string': 'Weteringschans 28, Bengaluru 1017 SG India'}, 'ancestors': [{'level': 'City', 'name': 'Bengaluru', 'location_id': '297628'}, {'level': 'District', 'name': 'Bangalore District', 'location_id': '12392950'}, {'level': 'State', 'name': 'Karnataka', 'location_id': '297627'}, {'level': 'Country', 'name': 'India', 'location_id': '293860'}], 'latitude': '12.98987', 'longitude': '77.59281', 'timezone': 'Asia/Kolkata', 'email': 'support@taxi2airport.com', 'phone': '+31 88 318 8344', 'website': 'https://www.taxi2airport.com', 'write_review': 'https://www.tripadvisor.com/UserReview-g297628-d20048279-Taxi2Airport_Bangalore-Bengaluru_Bangalore_District_Karnataka.html?m=66827', 'num_reviews': '0', 'photo_count': '23', 'see_all_photos': 'https://www.tripadvisor.com/Attraction_Review-g297628-d20048279-m66827-Reviews-Taxi2Airport_Bangalore-Bengaluru_Bangalore_District_Karnataka.html#photos', 'category': {'name': 'attraction', 'localized_name': 'Attraction'}, 'subcategory': [{'name': 'transportation', 'localized_name': 'Transportation'}, {'name': 'other', 'localized_name': 'Other'}, {'name': 'attractions', 'localized_name': 'Attractions'}], 'groups': [{'name': 'Other', 'localized_name': 'Other', 'categories': [{'name': '', 'localized_name': ''}]}, {'name': 'Transportation', 'localized_name': 'Transportation', 'categories': [{'name': 'Taxis & Shuttles', 'localized_name': 'Taxis & Shuttles'}]}], 'neighborhood_info': [], 'trip_types': [{'name': 'business', 'localized_name': 'Business', 'value': '0'}, {'name': 'couples', 'localized_name': 'Couples', 'value': '0'}, {'name': 'solo', 'localized_name': 'Solo travel', 'value': '0'}, {'name': 'family', 'localized_name': 'Family', 'value': '0'}, {'name': 'friends', 'localized_name': 'Friends getaway', 'value': '0'}], 'awards': []}"
ret = deep_search(["localized_name"], json.loads(json_string))
print (ret)
"""

"""
JSON = "{'location_id': '20048279', 'name': 'Taxi2Airport Bangalore', 'description': 'Taxi2Airport.com is an online reservation and booking system for airport transfers all around the globe. We are committed to providing safe and reliable transfers over all areas to and from all airports, cruise ports, and main train stations. Our service operates across 150+ countries and 1500+ airports with an excellent customer satisfaction rating of 4.5 out of 5 based on 35k+ reviews.', 'web_url': 'https://www.tripadvisor.com/Attraction_Review-g297628-d20048279-Reviews-Taxi2Airport_Bangalore-Bengaluru_Bangalore_District_Karnataka.html?m=66827', 'address_obj': {'street1': 'Weteringschans 28', 'city': 'Bengaluru', 'state': 'Karnataka', 'country': 'India', 'postalcode': '1017 SG', 'address_string': 'Weteringschans 28, Bengaluru 1017 SG India'}, 'ancestors': [{'level': 'City', 'name': 'Bengaluru', 'location_id': '297628'}, {'level': 'District', 'name': 'Bangalore District', 'location_id': '12392950'}, {'level': 'State', 'name': 'Karnataka', 'location_id': '297627'}, {'level': 'Country', 'name': 'India', 'location_id': '293860'}], 'latitude': '12.98987', 'longitude': '77.59281', 'timezone': 'Asia/Kolkata', 'email': 'support@taxi2airport.com', 'phone': '+31 88 318 8344', 'website': 'https://www.taxi2airport.com', 'write_review': 'https://www.tripadvisor.com/UserReview-g297628-d20048279-Taxi2Airport_Bangalore-Bengaluru_Bangalore_District_Karnataka.html?m=66827', 'num_reviews': '0', 'photo_count': '23', 'see_all_photos': 'https://www.tripadvisor.com/Attraction_Review-g297628-d20048279-m66827-Reviews-Taxi2Airport_Bangalore-Bengaluru_Bangalore_District_Karnataka.html#photos', 'category': {'name': 'attraction', 'localized_name': 'Attraction'}, 'subcategory': [{'name': 'transportation', 'localized_name': 'Transportation'}, {'name': 'other', 'localized_name': 'Other'}, {'name': 'attractions', 'localized_name': 'Attractions'}], 'groups': [{'name': 'Other', 'localized_name': 'Other', 'categories': [{'name': '', 'localized_name': ''}]}, {'name': 'Transportation', 'localized_name': 'Transportation', 'categories': [{'name': 'Taxis & Shuttles', 'localized_name': 'Taxis & Shuttles'}]}], 'neighborhood_info': [], 'trip_types': [{'name': 'business', 'localized_name': 'Business', 'value': '0'}, {'name': 'couples', 'localized_name': 'Couples', 'value': '0'}, {'name': 'solo', 'localized_name': 'Solo travel', 'value': '0'}, {'name': 'family', 'localized_name': 'Family', 'value': '0'}, {'name': 'friends', 'localized_name': 'Friends getaway', 'value': '0'}], 'awards': []}"
rex1  = re.compile('(?<=\"localized_name\": \")[a-zA-Z_\- ]+(?=\")')
rex2 = rex1.findall(JSON)
print(rex2)
"""


def findall(v, k):
    if type(v) == type({}):
        for k1 in v:
            if k1 == k:
                print (v[k1])
            findall(v[k1], k)
    if type(v) == type([]):
        for el in v:
            findall(el, k)


a = '{ "location_id": "6920077", "name": "The Ambience", "web_url": "https://www.tripadvisor.com/Attraction_Review-g297628-d6920077-Reviews-The_Ambience-Bengaluru_Bangalore_District_Karnataka.html?m=66827", "address_obj": { "street1": "#38 Cunningham Road", "street2": "Opp KFC Next Chai Point", "city": "Bengaluru", "state": "Karnataka", "country": "India", "postalcode": "560052", "address_string": "#38 Cunningham Road Opp KFC Next Chai Point, Bengaluru 560052 India" }, "ancestors": [ { "level": "City", "name": "Bengaluru", "location_id": "297628" }, { "level": "District", "name": "Bangalore District", "location_id": "12392950" }, { "level": "State", "name": "Karnataka", "location_id": "297627" }, { "level": "Country", "name": "India", "location_id": "293860" } ], "latitude": "12.99045", "longitude": "77.59163", "timezone": "Asia/Kolkata", "email": "ambience_art@yahoo.co.in", "phone": "+91 98804 85382", "write_review": "https://www.tripadvisor.com/UserReview-g297628-d6920077-The_Ambience-Bengaluru_Bangalore_District_Karnataka.html?m=66827", "ranking_data": { "geo_location_id": "297628", "ranking_string": "#199 of 234 Shopping in Bengaluru", "geo_location_name": "Bengaluru", "ranking_out_of": "234", "ranking": "199" }, "rating": "3.0", "rating_image_url": "https://www.tripadvisor.com/img/cdsi/img2/ratings/traveler/3.0-66827-5.svg", "num_reviews": "9", "review_rating_count": { "1": "5", "2": "0", "3": "0", "4": "0", "5": "4" }, "photo_count": "12", "see_all_photos": "https://www.tripadvisor.com/Attraction_Review-g297628-d6920077-m66827-Reviews-The_Ambience-Bengaluru_Bangalore_District_Karnataka.html#photos", "hours": { "periods": [ { "open": { "day": 1, "time": "0900" }, "close": { "day": 1, "time": "0900" } }, { "open": { "day": 2, "time": "0900" }, "close": { "day": 2, "time": "0900" } }, { "open": { "day": 3, "time": "0900" }, "close": { "day": 3, "time": "0900" } }, { "open": { "day": 4, "time": "0900" }, "close": { "day": 4, "time": "0900" } }, { "open": { "day": 5, "time": "0900" }, "close": { "day": 5, "time": "0900" } }, { "open": { "day": 6, "time": "0900" }, "close": { "day": 6, "time": "0900" } }, { "open": { "day": 7, "time": "0900" }, "close": { "day": 7, "time": "0900" } } ], "weekday_text": [ "Monday: 09:00 - 09:00", "Tuesday: 09:00 - 09:00", "Wednesday: 09:00 - 09:00", "Thursday: 09:00 - 09:00", "Friday: 09:00 - 09:00", "Saturday: 09:00 - 09:00", "Sunday: 09:00 - 09:00" ] }, "category": { "name": "attraction", "localized_name": "Attraction" }, "subcategory": [ { "name": "shopping", "localized_name": "Shopping" } ], "groups": [ { "name": "Shopping", "localized_name": "Shopping", "categories": [ { "name": "Gift & Specialty Shops", "localized_name": "Gift & Specialty Shops" } ] } ], "neighborhood_info": [], "trip_types": [ { "name": "business", "localized_name": "Business", "value": "2" }, { "name": "couples", "localized_name": "Couples", "value": "1" }, { "name": "solo", "localized_name": "Solo travel", "value": "4" }, { "name": "family", "localized_name": "Family", "value": "0" }, { "name": "friends", "localized_name": "Friends getaway", "value": "0" } ], "awards": [] }'
findall(json.loads(a), 'localized_name')
