# -*- coding: utf-8 -*

#Setup the home directory.
import os
os.chdir("C:")

"""
Please note the following:
1. Register your app at  :https://apps.twitter.com and get the security keys

2. install twitter python library : pip install twitter

3. API reference is https://dev.twitter.com/rest/public
"""

#Get these keys from your application. Please dont use the one
#that comes with the file

consumerKey = ''
consumerSecret = ''
OauthToken = ''
OauthSecret = ''

import twitter
import json

#Setup the Twitter API object
authInfo = twitter.oauth.OAuth(OauthToken, OauthSecret, consumerKey, consumerSecret)

twitterAPI = twitter.Twitter(auth=authInfo)

#Get My timeline
timeline= twitterAPI.statuses.home_timeline()

print json.dumps(timeline, indent=3)

for tweet in timeline:
    print"TWEET: ", tweet["text"]
    print "CREATED_AT: ", tweet["created_at"]
    for url in tweet["entities"]["urls"]:
        print"URL: ", url["expanded_url"]
        for description in tweet["description"]:
            print description["followers_count"]
        
    
#Get Others timeline
foxtweets=twitterAPI.statuses.user_timeline( \
        screen_name="FOXSports", count=1)

print json.dumps(foxtweets, indent=3)

#Extract text and also the user mentions
for tweet in foxtweets:
    print"TEXT: ",  tweet["text"]
    for mentions in tweet["entities"]["user_mentions"]:
        print "MENTION screen name:  " , mentions["screen_name"]
        print "HASHTAGS: ", mentions["hashtags"]
        
#search twitter
searchResults = twitterAPI.search.tweets(q="#HurrcaneIrma",count=20)

print json.dumps(searchResults,indent=3)
#Save results to a file
searchFile = open("searchResults.json","w")
searchFile.write(json.dumps(searchResults,indent=3))

for tweet in searchResults["statuses"]:
    print  tweet["text"]
    
#get followers
followerList = twitterAPI.followers.list(\
    screen_name="YOOX", count=10)
    
for follower in followerList["users"]:
    print "1st level : ", follower["screen_name"],\
                follower["friends_count"]
    
    NdFollow=twitterAPI.followers.list(\
            screen_name=follower["screen_name"] \
                , count=10)
    for NdFollower in NdFollow["users"]:
        print "   2nd Level : ", \
            NdFollower["screen_name"], NdFollower["friends_count"]
