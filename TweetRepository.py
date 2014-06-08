#!/usr/bin/env python
# encoding: utf-8
"""
TweetRepository.py

Created by Erik Thoresen Haug on 2014-06-07.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

from pymongo import MongoClient

class tweetRepository():
	def __init__(self):
	    self.client = MongoClient()
	
	def insert(self, tweet):
		
		db = self.client.tweet_sentiment_db
		tweets = db.tweets
		tweets.insert(tweet)
		
	def getTweetsContaining(self, ticker):
		db = self.client.tweet_sentiment_db
		results = []
		for tweet in db.tweets.find({"text": {'$regex' : '(?i).*' + ticker + '.*'}}):
			results.append(tweet)
		return results
	
	
	def getAll(self):
		db = self.client.tweet_sentiment_db
		return db.tweets.find()

def main():
	client = MongoClient()
	db = client.tweet_sentiment_db
	db.tweets.remove()
	pass


if __name__ == '__main__':
	main()

