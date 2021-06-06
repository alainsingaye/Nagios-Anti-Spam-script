#!/usr/bin/python3

import os
import sys
import json

import requests

WORDPRESS_ADDRESS = 'http://172.16.215.161'

date = os.popen('date \'+%Y-%m-%dT%H:%M:00\' --date=\"$DATE 4 hours ago\"').read()

f = date.find('\n')
date_format = date[:f]

response = requests.get("{}/wp-json/wp/v2/comments?after={}".format(WORDPRESS_ADDRESS, date_format))

todos = json.loads(response.text)

nb_com = 0
for id in todos:
	 nb_com = nb_com + 1


if nb_com >= 10: #More than 10 comments in the last 4hours
	print('CRITICAL - Too many comments posts in the last 4 hours')
	sys.exit(2)
elif nb_com >= 4: #More than 4 comments in the last 4hours
	print('WARNING - Too many comments posts in the last 4 hours')
	sys.exit(1)
else:
	print('OK - No comments spam')
	sys.exit(0)
