import argparse # allows application to accept input filenames as arguments
import urllib

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def getSentimentScore(text):
"""
Gets sentiment score of a selected text

:param category: text to analyze
:returns: sentiment score for text
"""
	score = annotations.document_sentiment.score
	return score

def getSentimentMagnitude(text):
"""
Gets sentiment magnitude of a selected text

:param category: text to analyze
:returns: sentiment magnitude for text
"""
	magnitude = annotations.document_sentiment.magnitude
	return magnitude

def analyzeArticle(url):
"""
Runs sentiment analysis on the text of a url

:param category: url to analyze text of
:returns: sentiment analysis for url's text
"""
	text = urllib.urlopen('http://www.bbc.com/news/world-asia-41375302').read()
	print(text)