import requests
from bs4 import BeautifulSoup
import sys

def downloadUrl(url):
	assert url.startswith('http://www.reddit.com/r/learnprogramming/')
	headers = {
			'User-Agent': 'Web-crawler bot version 0.1'
		  }
	r = requests.get(url, headers=headers)
	if r.status_code != 200:
		raise Exception("Non-OK status code: {}".format(r.status_code))
	return r.text

def parseText(html):
	bs = BeautifulSoup(html)
	div_entry = bs.select('div.entry')
	'''for div in div_entry:
		print (div.p)'''
	links = bs.find_all('a', { "class": "title" })
	print (links)
	for link in links:
		print (link['href'])
	#return bs.select('body')[0].text

class Crawler(object):
	def __init__(self, start_url):
		print ('Crawler object created')
		self.start_url = start_url

	def crawl(self):
		print ('Crawl initiated at : {}'.format(self.start_url))
		current_page_url = self.start_url
		html = downloadUrl(current_page_url)
		bs = BeautifulSoup(html)
		links = bs.find_all('a', { "class": "title" })
		for link in links:
			print (link['href'])

if __name__ == '__main__':
	crawler = Crawler('http://www.reddit.com/r/learnprogramming/')
	crawler.crawl()
