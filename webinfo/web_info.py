#coding:utf-8

import requests,mmh3,codecs
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from webinfo import agent

def get_info(url):
		try:
			r = requests.get(url=url, headers=agent.User_Agent(), 
				timeout=5, verify=False)
			content = r.text
			try:
				title = BeautifulSoup(content, 'lxml').title.text.strip()
				return str(r.headers), content, title.strip('\n'), str(r.status_code)
			except:
				return str(r.headers), content, ''
		except Exception as e:
			pass

def get_iconhash(url):
	try:
		parsed_url = urlparse(url)
		base_url = parsed_url.scheme + "://" + parsed_url.netloc + "/"
		icon_url = base_url + "favicon.ico"
		_icon = mmh3.hash(codecs.lookup('base64').encode(requests.get(url=icon_url, headers=agent.User_Agent(), timeout=5, verify=False).content)[0])
		return _icon
	except Exception as e:
		pass

