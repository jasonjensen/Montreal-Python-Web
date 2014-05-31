# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import tweepy
import time

"""Build a network of friends starting from the Twitter user senjohnmccain."""

APIKey = "" # API key
APISecret = "" # API scret
aToken = "" # access token
aSecret = "" #access secret

# instantiate OAuthHandler and initialize it with your credentials
auth = tweepy.OAuthHandler(APIKey,APISecret)
auth.set_access_token(aToken,aSecret)
api = tweepy.API(auth)

# get the User object given a Twitter handle
twitUser = api.get_user("senjohnmccain")

print
print("screen_name: " + twitUser.screen_name)
print("Number of friends: " + str(twitUser.friends_count))

MAXDEPTH = 3
MAXFRIENDS = 3

networkDepth = 0
friendNetwork = {}
screen_name_list = [twitUser.screen_name]

print "start building network..."

while(networkDepth < MAXDEPTH):

    networkDepth += 1
    num_screen_names = len(screen_name_list)

    for i in range(0,num_screen_names):

        screen_name = screen_name_list[i]

        if screen_name in friendNetwork.keys():
            print "already processed friends of " + screen_name
            continue

        friendNetwork[screen_name] = []
        friendCount = 0
        print("processing friends of " + screen_name)

        # use pagination support to loop over MAXFRIENDS friends
        for friend in tweepy.Cursor(api.friends,screen_name=screen_name,\
                                                            retry_delay=15,\
                                                            retry_count=5).items():

                print friend.screen_name
                friendNetwork[screen_name].append(friend.screen_name)
                screen_name_list.append(friend.screen_name)

                friendCount += 1

                # we will stop after we've counted MAXFRIEND friends
                if(friendCount >= MAXFRIENDS):
                    break

                # sleep for a bit so as not to exceed the Twitter rate limit
                time.sleep(15)

    screen_name_list = screen_name_list[num_screen_names:]

for item in friendNetwork.items():
    print(item)

