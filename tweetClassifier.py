#!/usr/bin/env python
# encoding: utf-8
"""
textClassifier.py

Created by Erik Thoresen Haug on 2013-06-18.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import collections, itertools
import time
import random
import re
import json
import scipy
from numpy import array
import pickle
import tweetProcessing

def openClassifier(filename):
	fp= open(filename)
	classifier = pickle.load(fp)
	fp.close()
	return classifier

class tweetClassifier():
	
	def __init__(self):
		filename = 'pickle/IIS_alg.pickle'
		self.classifier = openClassifier(filename)
	
	def classifyTweet(self,tweet):
		text = tweetProcessing.processTweet(tweet['text'])
		stopset = []
		feats = tweetProcessing.getFeatureSet(text)
		sentiment = self.classifier.classify(feats)
		prob = self.classifier.prob_classify(feats)
		if prob.prob(sentiment) < 0.35:
			sentiment = 'neutral'
		if ('followed', 'by', 'POSPERCENT') in feats:
			sentiment = 'positive'
		return sentiment

