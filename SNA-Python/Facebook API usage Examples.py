# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------

             Social Media Analytics with Python
             Copyright : V2 Maestros @2016
                    
Code Samples :Using Facebook REST API 
-----------------------------------------------------------------------------
"""
#Setup the home directory.
import os
os.chdir("C:\Users\Cosimo\Desktop\UDEMY COURSES\SNA-Python")

"""
Please note the following:
1. Register your app at https://developers.facebook.com/apps/
 Get access token following http://nodotcom.org/python-facebook-tutorial.html

Alternatively you can get access token thru https://developers.facebook.com/tools/explorer

2. install facebook python library

pip install requests
pip install facebook-sdk

3. API reference is https://developers.facebook.com/tools/explorer
"""
import requests
import json
import facebook

#Get these keys from your application 
# Please dont use the one that comes with the file
accessToken="CAACEdEose0cBALMibjaQqOzcS44YIbcZBWR2ib46PrwvNBqzfBAjvhc3srwE4HKXlonllEkoYyHpWs2Ro9gQouKMWmGeeQvAerggiNapfYlb3ZCVuuZCrOK0MKMm41fGwit0FPzBENlmMuwT0b8dYgf953DMZCu0uBbNGazKGO8WislfuV1i6oeVJori6TLpJhGbhsdz7Hlm38NwaIRk"

#myself
baseURL = "https://graph.facebook.com/v2.5/me"
selfFields="id,name,about,age_range,birthday"
finalURL= baseURL + "?fields=" + selfFields \
             + "&access_token=" + accessToken
selfData=requests.get(finalURL).json()
print json.dumps(selfData, indent=3)

#get my friends
friendsFields="friends{age_range,birthday,gender,location}"
finalURL= baseURL + "?fields=" + friendsFields \
             + "&access_token=" + accessToken
friendsData=requests.get(finalURL).json()
print json.dumps(friendsData, indent=3)

for friend in friendsData["friends"]["data"]:
    
    #fields might be optional.
    gender= "N/A"
    location="N/A"
    if "gender" in friend:
        gender=friend["gender"]
    if "location" in friend:
        location=friend["location"]["name"]
    print gender, location

#user = Donald Trump
#Find events he is attending.
#find user ID using http://findmyfbid.com

baseURL = "https://graph.facebook.com/v2.5/153080620724"
eventFields="id,name,about,events.limit(10).fields(attending_count,start_time,description)"

finalURL= baseURL + "?fields=" + eventFields \
             + "&access_token=" + accessToken
events=requests.get(finalURL).json()

print json.dumps(events, indent=3)
for eventData in events["events"]["data"]:
    print eventData["start_time"] , " = " , eventData["attending_count"]

#Using the facebook SDK
graphAPI = facebook.GraphAPI(accessToken)

#get my data
print json.dumps(graphAPI.get_object("me"),\
             indent=3)

#get my connections
print json.dumps(graphAPI.get_connections("me","friends"),\
             indent=3)

#Get Trump's data
print json.dumps(graphAPI.get_object("153080620724"),\
             indent=3)

#Query for specific strings
print json.dumps(graphAPI.request("search",\
            {"q":"Messi","type":"page"}), indent=3)
            
            
            
            
