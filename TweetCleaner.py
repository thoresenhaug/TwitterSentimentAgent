#!/usr/bin/env python
# encoding: utf-8
"""
TweetCleaner.py

Created by Erik Thoresen Haug on 2014-06-07.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""
import datetime, time

def clean(tweet):
	cleanTweet = dict()
	cleanTweet["tweet_id"] = tweet["id"]
	cleanTweet['text'] = tweet['text']
	cleanTweet['created_at'] = tweet['created_at']
	cleanTweet['created_at_unix'] = int(time.mktime(time.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")))+2*3600
	cleanTweet['followers'] = tweet['user']['followers_count']
	cleanTweet['following'] = tweet['user']['friends_count']
	cleanTweet['user_id'] = tweet['user']['id'],
	
	return cleanTweet

def main():
	
	pass

if __name__ == '__main__':
	main()