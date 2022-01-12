#!/usr/bin/python

import requests
from xml.dom.minidom import parseString

email = 'email'
passwd = 'password'

response = requests.get('https://mail.google.com/mail/feed/atom', auth=(email, passwd))
dom = parseString(response.content)
count = dom.getElementsByTagName('fullcount')[0].childNodes[0].nodeValue
print('You got',count,'new mails','┘')