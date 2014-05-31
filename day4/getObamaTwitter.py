# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import tweepy

"""Authenticate to twitter and obtain the follower count,
    description and public tweets from the Twitter user,
    BarackObama."""

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

tweeter=api.get_user("BarackObama")

print "\nTweeter follower count: " + str(tweeter.followers_count)
print "Tweeter description: " + tweeter.description
print "\nHere come the tweets..."

tweets = api.user_timeline(id=tweeter.id,count=10)
for tweet in tweets:
    print "Tweet: " + tweet.text

