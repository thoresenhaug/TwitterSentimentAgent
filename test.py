#!/usr/bin/env python
# encoding: utf-8
"""
test.py

Created by Erik Thoresen Haug on 2014-06-08.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from TweetRepository import tweetRepository
from tweetClassifier import tweetClassifier

def main():
	repo = tweetRepository()
	classifier = tweetClassifier()
	results = repo.getTweetsContaining("aapl")
	for tweet in results:
		print tweet['text'], classifier.classifyTweet(tweet)
	pass


if __name__ == '__main__':
	main()

