# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------

             Social Media Analytics with Python
             Copyright : V2 Maestros @2016
                    
Code Samples :Sentiment Analysis 

Before starting, install package textblob
    pip install textblob
-----------------------------------------------------------------------------
"""
#Setup the home directory.
import os
os.chdir("C:\Users\kumaran\Dropbox\V2Maestros\Courses\Social Media Analytics\Python")


import httplib2
import json
import apiclient.discovery

#Get these keys from your application. Please dont use the one
#that comes with the file


API_KEY = 'AIzaSyDNNtMHstmaEm5DoNApt9ldpjYDGD7d_KA'
service = apiclient.discovery.build('plus', 'v1', http=httplib2.Http(),
developerKey=API_KEY)

#Find activities with "Trump" in them

from textblob import TextBlob
nextPageToken=""

#Get 100 activities. Since each request only gives you 20
#repeat 100 times

for x in range(0,5):
    
    activity_feed=service.activities().search(query="Trump",\
                maxResults=20, pageToken=nextPageToken).execute() 
    #Get next page token for doing next query      
    nextPageToken=activity_feed["nextPageToken"]
                
    for activity in activity_feed["items"]:
        #Convert text to a textblob and find polarity
        activityBlob=TextBlob(activity["object"]["content"])
        polarity= activityBlob.sentiment.polarity
        
        polarityString="NEUTRAL"
        if polarity > 0 :
            polarityString="POSITIVE"
        elif polarity < 0 :
            polarityString="NEGATIVE"
            
        print polarity, polarityString, activity["object"]["content"][:80]
        
