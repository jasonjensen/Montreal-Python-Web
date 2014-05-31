# coding: utf-8
# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import tweepy
import json

''' Authenticate to twitter, use the Twitter REST API to
    execute a search.'''

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

for tweet in tweepy.Cursor(api.search,
                            q="Montréal",
                            # q="Denis AND Coderre",
                            rpp=10,
                            delay = 10,
                            result_type="recent",
                            include_entities=True,
                            lang="en").items():
    #print("Tweet: {0}.".format(tweet.text.encode("ascii",errors="replace")))
    print("Tweet Status: {0}.".format(tweet['statuses']))
