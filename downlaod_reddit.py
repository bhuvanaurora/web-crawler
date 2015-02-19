import requests
from bs4 import BeautifulSoup
import sys

def downloadUrl(url):
	r = requests.get(url)
	if r.status_code != 200:
		raise Exception("Non-OK status code: {}".format(r.status_code))
	return r.text

def parseText(html):
	bs = BeautifulSoup(html)
	return bs.select('div.md')[1].text

if __name__ == '__main__':
	url = sys.argv[1]
	html = downloadUrl(url)
	print (parseText(html))
