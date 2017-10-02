from bs4 import BeautifulSoup
import urllib.request
import csv
import requests
import feedparser

def getCategoryUrl(category):
"""
Retrieves corresponding Google News URL for a given news category

:param category: Selected news category  
:returns: URL string for category
"""
	with open('data/newsUrls.csv', mode='r') as infile:
		reader = csv.reader(infile)
		categoryUrls = {row[0].replace('\ufeff', '') : row[1] for row in reader}
	if category in categoryUrls:
		return categoryUrls[category]

def getNewsHeadlines(url):
"""
Gives the top ten headlines for a news category given the url

:param url: URL of category page in Google News
:returns: List of headlines for news category
"""
	markup = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(markup, "lxml")
	headlines = [element.title.text for element in soup.findAll('item')][:10]
	return headlines

def getFirstNLinks(url,n):
"""
Gets the links to the first n news results for the query

:param query: The search request to be made
:returns: List of links for the first n results when searching the query
"""
	d = feedparser.parse(url)
	links = []
	for i in range(5):
		if (d.entries[i]!=''):
			links.append(d.entries[i].link)
	return links


if __name__ == '__main__':
	# url = getCategoryUrl('World')
	# print(getNewsHeadlines(url))
	# print(getFirstNLinks(url,1))



