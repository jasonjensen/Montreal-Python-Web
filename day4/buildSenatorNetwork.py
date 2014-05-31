#coding: utf-8
# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import tweepy
import time
import urllib2
from bs4 import BeautifulSoup
import sys
import re
import yaml
import pandas as pd

"""Build a network of U.S. Senators on Twitter."""

ckey = "" #consumer key
csecret = "" #conumer scret
atoken = "" # access token
asecret = "" #access secret

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)

df = pd.DataFrame(columns=["TwitterUser1","TwitterUser2"])

# read in the YAML file to get Twitter handles of all the senators
yamlURL= "https://www.govtrack.us/data/congress-legislators/legislators-social-media.yaml"
yamlArray = yaml.load(urllib2.urlopen(yamlURL).read())

# senators is the map from the Senator's bioguide ID to the Twitter handle
senators = {}
for leg in yamlArray:
    try:
        senators[leg["social"]["twitter"]] = leg["id"]["bioguide"]
    except:
        print("Couldn't find all the information about legislator %s" % leg["id"]["bioguide"])
        pass

twitUser = api.get_user("SenatorCardin")

networkDepth = 0
friendNetwork = {}
edgeList = []
screen_name_list = [twitUser.screen_name]

MAXDEPTH = 2
MAXFRIENDS = 3

while networkDepth < MAXDEPTH:

    networkDepth += 1
    num_screen_names = len(screen_name_list)

    for i in range(0,num_screen_names):

        twitHandle = screen_name_list[i]

        if twitHandle in friendNetwork.keys():
            print "already processed friends of " + screen_name
            continue

        friendNetwork[twitHandle] = []
        friendCount = 0
        print("=====================================")
        print("Processing friends of " + twitHandle)

        # use pagination support to loop over MAXFRIENDS friends
        for friend in tweepy.Cursor(api.friends,screen_name=twitHandle,retry_delay=10).items():
            # print("Processing friend %s." % friend.screen_name)

            if(friend.screen_name in senators.keys()):
                friendNetwork[twitHandle].append(friend.screen_name)
                df = df.append({"TwitterUser1":twitHandle,
                                "TwitterUser2":friend.screen_name},
                                    ignore_index=True)
                friendCount += 1
                screen_name_list.append(friend.screen_name)

                # we will stop after we've counted MAXFRIEND friends
                if(friendCount >= MAXFRIENDS):
                    break

            # sleep for a bit so as not to exceed the Twitter rate limit
            time.sleep(3)

        screen_name_list = screen_name_list[num_screen_names:]

print(df)
