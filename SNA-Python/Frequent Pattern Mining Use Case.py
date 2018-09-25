# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------

             Social Media Analytics with Python
             Copyright : V2 Maestros @2016
                    
Code Samples :Frequent Pattern Mining

Understand which users are mentioned frequently together.
-----------------------------------------------------------------------------
"""
#Setup the home directory.
import os
os.chdir("C:\Users\kumaran\Dropbox\V2Maestros\Courses\Social Media Analytics\Python")

#Get these keys from your application. Please dont use the one
#that comes with the file

consumerKey = 'xllG74V8bklytXuh9U2InA9eV'
consumerSecret = 'Qm4HRLPguwPyUtbL1h8bWeAujeh3gy0rVUahfgbJL9yIiuDNCP'
OauthToken = '713039024550588416-Jsi8LBxQk41EB83wJihTHdBKwtWlghZ'
OauthSecret = '5DfrNVgwcXVXALjCDM49F8QN1LN7tGo8vGcBBpPq1UDoJ'

import twitter
import json

#Setup the Twitter API object
authInfo = twitter.oauth.OAuth(OauthToken, OauthSecret,
                           consumerKey, consumerSecret)
twitterAPI = twitter.Twitter(auth=authInfo)
    
import pandas as pd

#Set to a very large ID
maxId=9171891474970910721

basket=""
#Collect last 1000 tweets and create a basket of 
#user mentions that occur together.
#the basket has one record per tweet with all user mentions
#seperated by commas

for x in range(0,5):
    
    newsTweets=twitterAPI.statuses.user_timeline( \
        screen_name="FoxNews", \
        exclude_replies=True, \
        max_id=maxId - 1, \
         count=200)
        
    for tweet in newsTweets:
        
        #Keep track of last ID
        max_id = tweet["id"]
        mentionStr=""
        #Extract user mentions and create a comma seperated string
        for mentions in tweet["entities"]["user_mentions"]:
            #print mentions["screen_name"]
            if mentionStr != "":
                mentionStr = mentionStr + ","
            mentionStr = mentionStr + mentions["screen_name"]
        #if string not empty then add to basket
        if mentionStr != "":
            basket = basket + mentionStr + "\n"
        
        
        
        
print basket   
#Save the basket to a file for future use.
basket_file=open("mention_basket.csv","w")
basket_file.write(basket)
basket_file.close()     

import csv
with open('mention_basket.csv', 'rb') as f:
    reader = csv.reader(f)
    basket_list = list(reader)

basket_dict = dict()
 #Build a dictionary with occurances first.
for rec in basket_list:
     for user in rec:
         if  basket_dict.has_key(user) == False :
             basket_dict[user] = dict(count=0, link= dict() )
         basket_dict[user]["count"] +=1
         
print basket_dict

#now find link counts
for user in basket_dict:
    for rec in basket_list:
        if user in rec:
            for other_user in rec:
                if user != other_user:
                    if basket_dict[user]["link"].has_key(other_user) == False:
                        basket_dict[user]["link"][other_user]=0;
                    basket_dict[user]["link"][other_user] +=1

print basket_dict
support =0.5

#Check pattern if where support is greater than set value
for user in basket_dict:
    for userlink in basket_dict.get(user).get("link"):
        together = basket_dict.get(user).get("link").get(userlink) \
                    * 1.0 /  basket_dict.get(user).get("count")
        if  together > support :
            print user, basket_dict.get(user).get("count"),  " => ", userlink, " - ", together
 



    
    
