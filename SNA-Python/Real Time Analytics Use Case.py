# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------

             Social Media Analytics with Python
             Copyright : V2 Maestros @2016
                    
Code Samples :Real Time Analysis - Sentiment Analysis

Before starting, install package textblob
    pip install textblob
-----------------------------------------------------------------------------
"""
#Setup the home directory.
import os
os.chdir("C:\Users\kumaran\Dropbox\V2Maestros\Courses\Social Media Analytics\Python")

consumerKey = 'xllG74V8bklytXuh9U2InA9eV'
consumerSecret = 'Qm4HRLPguwPyUtbL1h8bWeAujeh3gy0rVUahfgbJL9yIiuDNCP'
OauthToken = '713039024550588416-Jsi8LBxQk41EB83wJihTHdBKwtWlghZ'
OauthSecret = '5DfrNVgwcXVXALjCDM49F8QN1LN7tGo8vGcBBpPq1UDoJ'

import twitter
import json

authInfo = twitter.oauth.OAuth(OauthToken, OauthSecret,
                           consumerKey, consumerSecret)
twitterAPI = twitter.Twitter(auth=authInfo)

from textblob import TextBlob
import sys

twitter_stream=twitter.TwitterStream(auth=authInfo, \
        domain="userstream.twitter.com")
iterator=twitter_stream.user()
for tweet in iterator:
    if "text" in tweet:
        tweetText=tweet["text"]
        activityBlob=TextBlob(tweetText)
        polarity= activityBlob.sentiment.polarity
        
        polarityString="NEUTRAL"
        if polarity > 0 :
            polarityString="POSITIVE"
        elif polarity < 0 :
            polarityString="NEGATIVE"
            
        print polarityString, tweetText
        print "----------"
        sys.stdout.flush()
