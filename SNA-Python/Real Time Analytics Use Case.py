# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------
Before starting, install package textblob

pip install textblob
-----------------------------------------------------------------------------
"""
#Setup the home directory.
import os
os.chdir("C:")

consumerKey = ''
consumerSecret = ''
OauthToken = ''
OauthSecret = ''

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
