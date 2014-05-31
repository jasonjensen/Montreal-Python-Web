# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import tweepy
import time

"""Print out screen names of friends of Twitter user senjohnmccain."""

APIkey = "" #API key
APIsecret = "" #API scret
atoken = "" # access token
asecret = "" #access secret

# instantiate OAuthHandler and initialize it with your credentials
auth = tweepy.OAuthHandler(APIkey,APIsecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)

# get the User object given a Twitter handle
twitUser = api.get_user("senjohnmccain")

print
print("screen_name: " + twitUser.screen_name)
print("Number of friends: " + str(twitUser.friends_count))

print
print("senjohnmccain's first 30 friends are:")

#for friend in twitUser.friends():
#   print friend.screen_name

friendCount = 0

# use pagination support to loop over *all* the friends
for friend in tweepy.Cursor(api.friends,id=twitUser.id,retry_delay=10).items():

    print friend.screen_name
    friendCount += 1

    # we will stop after we've counted 30 friends
    if(friendCount == 30):
        break

    # sleep for a bit so as not to exceed the Twitter rate limit
    time.sleep(5)
