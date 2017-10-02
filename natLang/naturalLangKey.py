from watson_developer_cloud import NaturalLanguageUnderstandingV1

def enableWatsonNatLang():
"""
Returns instance of Natural Language processing Understanding Object to enable natural language processing through IBM Watson

param: none
returns: Natural Language processing Understanding Object
"""
	return NaturalLanguageUnderstandingV1(
	  username="8e11eecb-d9e3-4a63-9ea8-740fe63adfb6",
	  password="R8C3WkuIXfep",
	  version="2017-02-27")