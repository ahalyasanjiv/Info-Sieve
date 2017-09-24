import argparse # allows application to accept input filenames as arguments

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

"""
Gets sentiment score of a selected text

:param category: text to analyze
:returns: sentiment score for text
"""
def getSentimentScore(text):
	score = annotations.document_sentiment.score
	return score

"""
Gets sentiment magnitude of a selected text

:param category: text to analyze
:returns: sentiment magnitude for text
"""
def getSentimentMagnitude(text):
	magnitude = annotations.document_sentiment.magnitude
	return magnitude

"""
Runs sentiment analysis on the text of a url

:param category: url to analyze text of
:returns: sentiment analysis for url's text
"""
def analyzeArticle(url):
	pass

