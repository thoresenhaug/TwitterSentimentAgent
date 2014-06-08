#!/usr/bin/env python
# encoding: utf-8
"""
tweetProcessing.py

Created by Erik Thoresen Haug on 2014-06-08.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import re
import json
import nltk
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist

def processTweet(tweet):
	# process the tweets
	#Convert to lower case
	tweet = tweet.lower()

	tweet = tweet.replace(':)',' SMILEYUP ').replace(':-)',' SMILEYUP ').replace('=D',' SMILEYUP ').replace('8-)',' SMILEYUP ').replace(':D',' SMILEYUP ').replace('=]',' SMILEYUP ').replace('\u263a',' SMILEYUP ')
	tweet = tweet.replace(':(',' SMILEYDOWN ').replace('8-(',' SMILEYDOWN ').replace(';-(',' SMILEYDOWN ').replace(';(',' SMILEYDOWN ').replace(':-(',' SMILEYDOWN ')
	tweet = tweet.replace(';o)',' SMILEYWINK ').replace(';-)',' SMILEYWINK ').replace(';)',' SMILEYWINK ')
	tweet = tweet.replace('???',' XQUESTIONX ').replace('??',' XQUESTIONX ').replace('?',' XQUESTIONX ').replace('!',' ')


	tweet = tweet.replace('n\'t',' not ').replace('cant ','can not ').replace(' isnt ',' is not ')
	tweet = tweet.replace(' it\'s ',' it is ').replace('i\'m ','I am ').replace('i\'ll ','I will ').replace(' & ',' and ')
	
	tweet = re.sub('[$]\d+.\d+','DOLLARNUMBER ',tweet)
	tweet = re.sub('-\d+(?:\.\d+)?%','NEGPERCENT ',tweet)
	tweet = re.sub('[+]?\d+(?:\.\d+)?%','POSPERCENT ',tweet)
	tweet = re.sub('-\d+(?:\.\d+)','NEGDECIMAL ',tweet)
	tweet = re.sub('[+]?\d+(?:\.\d+)','POSDECIMAL ',tweet)
	
	#Convert www.* or https?://* to URL
	tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
	#Convert @username to AT_USER
	tweet = re.sub('@[^\s]+','AT_USER',tweet)
	#Convert $ticker to TICKER
	tweet = re.sub('\$[a-z]+','TICKER',tweet)
	tweet = tweet.replace(',',' ').replace('.',' ').replace(':',' ')
	#Remove additional white spaces
	tweet = re.sub('[\s]+', ' ', tweet)
	#Replace #word with word
	tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	#trim
	tweet = tweet.strip('\'"')
	

	return tweet

def getStopSet():
	stopWords = []
	stopWords = stopwords.words('english')
	stopWords.append('AT_USER')
	stopWords.append('URL')
	stopWords.append('TICKER')
	stopWords.append('DOLLARNUMBER')
	stopWords.append('POSPERCENT')
	stopWords.append('NEGPERCENT')
	stopWords.append('POSDECIMAL')
	stopWords.append('NEGDECIMAL')
	stopWords.append('rsi')
	stopWords.append('ret')
	return set(stopWords)

def getFeatureSet(text):
	def word_feats(words):
		return dict([(word, True) for word in words])
	
	def best_bigram_word_feats(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
		bigram_finder = BigramCollocationFinder.from_words(words)
		bigrams = bigram_finder.nbest(score_fn, n)
		d = dict([(bigram, True) for bigram in bigrams])
		
		return d
	
	def best_tri_and_bigram_word_feats(words, score_fn=TrigramAssocMeasures.chi_sq, n=200):
		trigram_finder = TrigramCollocationFinder.from_words(words)
		trigrams = trigram_finder.nbest(score_fn, n)
		d = dict([(trigram, True) for trigram in trigrams])
		d.update(word_feats(words))
		return d
	
	words_filtered = [e for e in nltk.word_tokenize(text)]
	feats = best_tri_and_bigram_word_feats(words_filtered)
	return feats


def main():
	pass


if __name__ == '__main__':
	main()

