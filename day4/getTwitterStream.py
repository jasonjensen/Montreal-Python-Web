#coding: utf-8

# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import time

"""Print out raw tweets containing the text "Obamacare"
    obtained from the Twitter stream"""

APIkey = "" #API key
APIsecret = "" #API scret
atoken = "" # access token
asecret = "" #access secret

# extend tweepy's StreamListener class and re-define the on_data() method
class SListener(StreamListener):

    def on_data(self,data):
        """Called when raw data is received from the Stream."""
        try:
            if "limit" in data:
                return False
            else:
                print
                print(data)
                time.sleep(2)
                return True
        except:
            print "Exception encountered while processing tweets."
            time.sleep(5)

if __name__=="__main__":

    # instantiate OAuthHandler and initialize it with your credentials
    auth = OAuthHandler(APIkey,APIsecret)
    auth.set_access_token(atoken,asecret)

    # instantiate an instance of the new SListener class
    myListener = SListener()
    twitterStream = Stream(auth,myListener)
    twitterStream.filter(track=["Obamacare"])
