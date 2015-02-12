#!/usr/bin/python
# -*- coding: utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import re
import sys

consumer_key="Aon0bjz4YJrSvK5AaYOmaA"
consumer_secret="ok6n7nLFnTK7sPgfJy9KePVWWpNLsf66ZjG2qxybE"

access_token="702257119-3JFCScVL8HSioH3TwxEvgXESsLFcRrGSrmFHXnV6"
access_token_secret="lA1fKzQbHMJWtPYdhcgOYTtFnyhuob16ItiWHO6hw"

CUTOFF = -1

class StdOutListener(StreamListener):

    count = 0

    def on_data(self, data):
        tweet = json.loads(data)

        if self.count == CUTOFF : exit(0)

        if "lang" in tweet["user"] and tweet["user"]["lang"] == "en":
            print "\t".join([tweet["text"],tweet["user"]["screen_name"]]).encode('ascii', 'ignore').replace('\n', ' ')
	    self.count += 1

        return True

    def on_error(self, status):
        print 'Error: ', status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)

    if len(sys.argv) < 2 : 
	print 'USAGE : python get_tweets.py [n] [keyword1 keyword2 ... keywordn]'
	exit(0)

    try : 
	CUTOFF = int(sys.argv[1])
    	company_names = sys.argv[2:]
    except : company_names = sys.argv[1:]

    stream.filter(track=company_names)





