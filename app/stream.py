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
		self.name = name

class StdOutListener(StreamListener):
    def on_data(self, data):
        data = json.loads(data)
        with open('fetched_tweets.txt','a') as f:
            f.write(data['text']+'\n<BREAK>\n')
        return True

    def on_error(self, status):
        print status

def main():
    # create stream to Twitter API
    stream = connect()
    # read / save world leaders data
    leaders = read()
    # run stream filtering world leader names
    stream.filter(track=leaders.names())

def connect():
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return Stream(auth, l)

def read():
    leaders = Leaders()
    with codecs.open(os.path.dirname(__file__) + "/../leaders.txt".format(file), encoding='utf-8') as f:
        for line in f.readlines():
            if len(line.split(', ')) == 3:
                leaders.add(Leader(*line.split(', ')))
    return leaders

if __name__ == '__main__':
    main()
