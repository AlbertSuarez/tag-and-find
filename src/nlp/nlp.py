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
    for sentences in sentences:
        entities = get_entities(sentences)
        word_dict = assign_pol(entities)