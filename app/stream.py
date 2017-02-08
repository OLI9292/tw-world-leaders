#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

import codecs
import json
import os
import os.path
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from flask import g

ACCESS_TOKEN = '758586954539732992-oLPy6ZKtdFuFSdkvfxMdqkjjFFDx2RU'
ACCESS_TOKEN_SECRET = 'BojAqDw4q1h8J4ZeGghlOoBgfcka3f5Wn10IX1eNB9sI2'
CONSUMER_KEY = 'GvkjcL1Z1KX9bFtWdflH0F4Hs'
CONSUMER_SECRET = '0ArbTqJusB6MXW4TQvrDhfl6wYe180ABjSfA6XCF2P401mJ90f'

class Leader:
  def __init__(self, country, position, name):
    self.country = country
    self.position = position
    self.name = name

class StdOutListener(StreamListener):
  def on_data(self, data):
    data = json.loads(data)
    if 'text' in data.keys():
      print data['text']
    return True
  def on_error(self, status):
    print status

def stream():
  # create stream to Twitter API
  stream = connect()
  # read / save world leaders data
  leaders = read_data()
  # run stream filtering world leader names
  stream.filter(track = [l.name for l in leaders])

def connect():
  l = StdOutListener()
  auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  return Stream(auth, l)

def read_data():
  leaders = []
  leaders_data = os.path.dirname(__file__) + "/../leaders.txt".format(file)
  with codecs.open(leaders_data, encoding='utf-8') as f:
    for line in f.readlines():
      if len(line.split(', ')) == 3:
        formatted = line.rstrip().split(', ')
        leaders.append(Leader(*formatted))
  return leaders

if __name__ == '__main__':
  stream()
