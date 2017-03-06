#!/usr/bin/python3

import datetime
import urllib.request
from bs4 import BeautifulSoup

class WikiCrawler:

	def __init__(self, url, host, sampleData):
		self.url = url
		self.host = host
		self.sampleData = sampleData

	#The Url requester make http call and get the data back and convert it into html elments using beautifulsoup lib
	def urlRequester(self):
		try:
			print('Requesting url -----',self.url)
			response = urllib.request.urlopen(self.url)
			soup = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
			#soup = BeautifulSoup(self.sampleData, 'html.parser')
			langElements = soup.select("div.div-col a")
			return langElements
		except Exception as e:
			raise Exception(e)

	# Thie method frame the insert document type using crawling data
	def makeValueList(self, elements):
		try:
			ls = []
			for element in elements:
				c = (element.string,element['href'],self.host)
				ls.append(c)
			return ls
		except Exception as e:
			raise Exception(e)

if __name__ == "__main__" :
	crawler = WikiCrawler("https://en.wikipedia.org/wiki/List_of_programming_languages","https://en.wikipedia.org")
	rawData = crawler.urlRequester()
	sqlLiteQueryStr = crawler.queryBuilder(rawData, 'computer_langues')

