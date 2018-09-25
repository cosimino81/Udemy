# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------

             Social Media Analytics with Python
             Copyright : V2 Maestros @2016
                    
Code Samples :Frequency Analysis 
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
    
#Create an empty Data Frame
import pandas as pd

colList=["Lang","TimeZone","Friends"]
followDF =  pd.DataFrame(columns=colList)
next_cursor=-1

    #Get followers of HP get 1000. Loop 5 times since
    # max count is 200
for x in range(0,5):
    followerList = twitterAPI.followers.list(\
        screen_name="HP", cursor=next_cursor, count=200)
        
    next_cursor=followerList["next_cursor"]

    for follower in followerList["users"]:
        followDF=followDF.append(pd.Series([follower["lang"],\
                       follower["time_zone"],\
                       follower["friends_count"]] ,\
                       index=colList ),\
                       ignore_index=True)

#Analyze the data frame created
followDF.count()

langGroup=followDF.groupby(followDF.Lang)
langGroup.describe()

timezoneGroup=followDF["Friends"].groupby(followDF.TimeZone)
timezoneGroup.describe()
timezoneGroup.count()
timezoneGroup.mean()