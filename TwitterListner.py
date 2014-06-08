#!/usr/bin/env python
# encoding: utf-8
"""
TwitterListner.py

Created by Erik Thoresen Haug on 2014-06-07.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

from tweepy.streaming import StreamListener
from TweetRepository import tweetRepository

import TweetCleaner
import time
import json
	
from tweetClassifier import tweetClassifier

class tweetListner(StreamListener):
	def __init__(self):
	    self.repo = tweetRepository()
	
	def on_data(self, data):
		try:
			tweet = TweetCleaner.clean(json.loads(data))
			classifier = tweetClassifier()
			tweet['sentiment'] = classifier.classifyTweet(tweet);
			self.repo.insert(tweet)
			print 'Tweet was inserted into the database', tweet
			return True
		except BaseException, e:
			print 'Failed on_data', str(e)
			time.sleep(5)
			
		

	def on_error(self, status):
		print status
		

