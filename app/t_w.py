#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

import codecs
import json
import os.path
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

ACCESS_TOKEN = "758586954539732992-oLPy6ZKtdFuFSdkvfxMdqkjjFFDx2RU"
ACCESS_TOKEN_SECRET = "BojAqDw4q1h8J4ZeGghlOoBgfcka3f5Wn10IX1eNB9sI2"
CONSUMER_KEY = "GvkjcL1Z1KX9bFtWdflH0F4Hs"
CONSUMER_SECRET = "0ArbTqJusB6MXW4TQvrDhfl6wYe180ABjSfA6XCF2P401mJ90f"

class Leaders:
	def __init__(self):
		self.leaders = []

	def add(self, leader):
		self.leaders.append(leader)

	def countries(self):
		return [x.country for x in self.leaders]

	def names(self):
		return [x.name for x in self.leaders]

	def all(self):
		return self.leaders

class Leader:
	def __init__(self, country, position, name):
		self.country = country
		self.position = position
		self.name = name.replace('\n', '')

class StdOutListener(StreamListener):
    def on_data(self, data):
    	data = json.loads(data)
        for x in data:
        	print x, ': ', data[x]
        print '\n\n\n\n'
        return True
    def on_error(self, status):
        print status

def hi():
	stream.filter(track=['president'])

def main(file):
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)
    leaders = Leaders()
    with codecs.open(os.path.dirname(__file__) + "/../{0}".format(file), encoding='utf-8') as f:
        for line in f.readlines():
            if len(line.split(', ')) == 3:
                leaders.add(Leader(*line.split(', ')))
    stream.filter(track=leaders.names())

if __name__ == '__main__':
    main()
