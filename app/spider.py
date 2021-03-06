#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

import requests
from bs4 import BeautifulSoup
import re
import codecs

STATE_LEADERS_URL = 'https://en.wikipedia.org/wiki/List_of_current_heads_of_state_and_government'
HEADERS = ['State', 'Head of state', 'Head of government']

def main():
  data = retrieve()
  data = parse(data)
  write(data)

def retrieve():
  page = requests.get(STATE_LEADERS_URL)
  encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
  soup = BeautifulSoup(page.content, 'html.parser',from_encoding = encoding)
  data = soup.find('table', class_= 'wikitable plainrowheaders')
  if all(h in data.find('tr').text for h in HEADERS):
    return data
  raise Exception('Unexpected body content from url.')

def parse(data):
  parsed_data = []
  for row in data.find_all('tr')[1:]:
    if hasattr(row.find('th'), 'text'):
      country = clean(row.find('th').text).encode('utf-8')
    cells = [clean(c.text).encode('utf-8') for c in row.find_all('td') if hasattr(c, 'text')]
    for cell in cells:
      text = re.split('\xc2\xa0\xe2\x80\x93 ', cell)
      if len(text) != 2:
        continue
      position, name = re.split('\xc2\xa0\xe2\x80\x93 ', cell)
      name = name.replace('\n', '')
      parsed_data.append([country, position, name])
  return parsed_data

def clean(text):
  return text.strip().split('[', 1)[0]

def write(data):
  with codecs.open('leaders.txt', 'w', 'utf-8-sig') as f:
    for row in data:
      f.write("{0}\n".format(', '.join(row)))  

if __name__ == '__main__':
  main()
