import json
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import watson_developer_cloud.natural_language_understanding.features.v1 as Features
import naturalLangKey as nl

"""
Used to see if the tag is part of main text of page or not

:param: element: HTML tag element to check
:returns: Boolean value denoting whether tag element should be include
"""
def includeTag(element):
    if isinstance(element, Comment) or element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    return True

"""
Extracts text from HTML page

:param: html: HTML of page to get text from
:returns: Plain text extracted from html
"""
def text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    # Parse text for HTML elements that do not contain the main text of the page
    visible_texts = filter(includeTag, texts)  
    return u" ".join(t.strip() for t in visible_texts)

"""
Get sentiment analysis of a given URL

:param: url: URL to get sentiment analysis
:returns: Sentiment magnitude and emotion analysis in JSON format
"""
def getSentimentAnalysis(url):
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	text = text_from_html(html)
	natural_language_understanding = nl.enableWatsonNatLang()
	response = natural_language_understanding.analyze(
		text= text,
	  	features=[
	    Features.Entities(
	      emotion=True,
	      sentiment=True,
	      limit=2
	    )
	  	]
	)
	return json.dumps(response, indent=2)

if __name__ == '__main__':
	# Test functionality of sentiment analysis
	url = "https://www.washingtonpost.com/powerpost/cassidy-on-new-health-care-plan-its-not-for-susan-its-for-the-mainers/2017/09/25/3dc5d74e-a20f-11e7-b14f-f41773cd5a14_story.html"
	print(getSentimentAnalysis(url))
