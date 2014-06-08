#!/usr/bin/env python
# encoding: utf-8
"""
TwitterAgent.py

Created by Erik Thoresen Haug on 2014-06-07.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

from tweepy import Stream
from tweepy import OAuthHandler
from TwitterListner import tweetListner
from tweepy.streaming import StreamListener

def GetStream(filters):
	auth = GetAuthentication()
	twitterStream = Stream(auth, tweetListner())
	twitterStream.filter(track=filters)

def GetAuthentication():
	
	consumer_key = 'dc3XdT2RJoW8bEyH3HeZfg'
	consumer_secret = '25498fH6gnvLQJZVzSqvBaSINveeE82UC18nLe2yzAU'
	access_token = '146400009-xVHXPOQOitcxXJ6nwofi8tqTTLI8HBD8IFysPvnc'
	access_token_secret = 'Wu3zEhdOrmnMF5XMAAXjf43J9YUuo0A8a80QMdxPk'
	
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	return auth

def StartAgent():
	search_queries = ['$F','$FB','$GOOG','$MSFT','$AAPL','$INTC','$TSLA','$GE','$AMZN','$YHOO','$DDD','$PFE','$EBAY','$FSLR','$CSCO','$QQQ','$ORCL','$GRPN','$ZNGA']
	stream = GetStream(search_queries)

def main():
	StartAgent()
	pass


if __name__ == '__main__':
	main()
