# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------

             Social Media Analytics with Python
             Copyright : V2 Maestros @2016
                    
Code Samples :Using Google+ REST API 
-----------------------------------------------------------------------------
"""
#Setup the home directory.
import os
os.chdir("C:\Users\kumaran\Dropbox\V2Maestros\Courses\Social Media Analytics\Python")

"""
Please note the following:
1. Register your app at https://console.developers.google.com/apis

2. Enable Google+ APIs

3. Generate an API Key for your application

4. install google+ python library

pip install google-api-python-client

3. API reference is https://developers.google.com/+/web/api/rest/latest/
"""
#enable google+
#create API key as browser key
#Get these keys from your application. Please dont use the one
#that comes with the file

import httplib2
import json
import apiclient.discovery

API_KEY = 'AIzaSyDNNtMHstmaEm5DoNApt9ldpjYDGD7d_KA'
service = apiclient.discovery.build('plus', 'v1', http=httplib2.Http(),
developerKey=API_KEY)

#Find everyone whose name is kumaran
people_feed = service.people().search(query="kumaran",\
       maxResults=3 ).execute()
       
print json.dumps(people_feed['items'], indent=1)

#Query for each person and find their gender
for people in people_feed["items"]:
    print people["displayName"], people["id"]
    person_feed=service.people().get(userId=people["id"]).execute()
    print person_feed["gender"]
    
#Search for activities
activity_feed=service.activities().search(query="V2Maestros",\
            maxResults=5).execute()
            
print json.dumps(activity_feed,indent=1)

for activity in activity_feed["items"]:
    print activity["actor"]["displayName"], \
            activity["object"]["content"], \
            activity["object"]["plusoners"]["totalItems"]
    print "*********************************"
            
    #get comments for the activity
    comments_feed=service.comments().list( \
            activityId=activity["id"], \
            maxResults=5).execute()
   # print json.dumps(comments_feed, indent=1)
    for comment in comments_feed["items"]:
        print "COMMENT: ", comment["object"]["content"]
    
