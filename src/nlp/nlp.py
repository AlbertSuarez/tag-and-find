from textblob import TextBlob

def get_sentences(text):
    return text.sentences   


""" Given a sentence returns the topic """"
def get_topic(text):
    # Get nouns 
    array = []
    tokens = text.tags
    for key,value in tokens
        if value == 'ADJ'

def get_sentiment(text):
    return text.sentiment    