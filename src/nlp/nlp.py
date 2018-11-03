from textblob import TextBlob
from src.dialogflow  import dialogflow


def get_sentences(text):
    return text.sentences   


""" Given a sentence get the entities list"""
def get_topic(text):
    

def get_sentiment(text):
    return text.sentiment    

def get_entities(sentences): 
    # Get entities 
    return dialogflow.get_entities(str(sentences))

def from_text_return_dict(text):
    text_b = TextBlob(text)
    sentences = get_sentences(text_b)
    dict_words = {}
    for sentence in sentences:
        entities = get_entities(sentence)
        sent = get_sentiment(sentence)
        for entity in entities:
            dict_words[entity] = sentiment
    return dict_words


def get_top_entities_from_a_review(reviews):
    dict_words = {
        'list': []
    }
    for review in reviews:
        dict_aux = from_text_return_dict(review)
        