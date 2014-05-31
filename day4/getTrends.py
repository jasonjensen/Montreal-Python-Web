# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import tweepy
import json

''' Authenticate to Twitter and use the Twitter REST API
    to access location-based information on trending
    topics.'''

APIkey = "" #API key
APIsecret = "" #API scret
atoken = "" # access token
asecret = "" #access secret

# instantiate OAuthHandler and initialize it with your credentials
auth = tweepy.OAuthHandler(APIkey,APIsecret)
auth.set_access_token(atoken,asecret)

# instantiate the tweepy object, invoke the constructor with the just-created
# OAuthHandler object
api = tweepy.API(auth)

# initialize variables containing Where-On-Earth IDs of interesting locations
canada_woeid = 23424775
ukraine_woeid = 23424976
usa_woeid = 23424977
world_woeid = 1

'''
# Get locations that Twitter has trending topic information for
# https://dev.twitter.com/docs/api/1.1/get/trends/available
jsonResp = api.trends_available()
print(json.dumps(jsonResp,indent=4))
'''

'''
# Get locations that Twitter has trending topic info for, closest
# to a specified geo-location
# https://dev.twitter.com/docs/api/1.1/get/trends/closest
jsonResp = api.trends_closest(lat=45.4,long=-75.6667)
print(json.dumps(jsonResp,indent=4))
'''

# Get the top 10 trending topics for a specific WOEID
# https://dev.twitter.com/docs/api/1.1/get/trends/place
jsonResp = api.trends_place(canada_woeid)
print(json.dumps(jsonResp,indent=4))

