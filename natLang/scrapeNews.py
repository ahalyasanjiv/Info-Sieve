from bs4 import BeautifulSoup
import urllib.request
import csv

def getNewsHeadlines(url):
	markup = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(markup, "lxml")
	headlines = [element.title.text for element in soup.findAll('item')][:10]
	return headlines

def getTopicUrl(topic):
	with open('data/newsUrls.csv', mode='r') as infile:
		reader = csv.reader(infile)
		topicUrls = {row[0].replace('\ufeff', '') : row[1] for row in reader}
	if topic in topicUrls:
		return topicUrls[topic]

if __name__ == '__main__':
	url = getTopicUrl('World')
	print(getNewsHeadlines(url))

