from textblob import TextBlob
from src.nlp import entities


def get_sentences(text):
    return text.sentences   


def get_sentiment(text):
    return text.sentiment.polarity   


def from_text_return_dict(text):
    text_b = TextBlob(text)

    # Split in sentences
    sentences = get_sentences(text_b)
    dict_words = {}
    for sentence in sentences:
        # Get entities
        list_ent = entities.get_entities(sentence.words)
        # Assign sentiment score
        sent = get_sentiment(sentence)
        for entity in list_ent:
            dict_words[entity] = sent
    return dict_words


def update_score(dict_words, key, value):
    # If exist calculate the mean score
    if key in dict_words:
        dict_words[key]['list_score'].append(value)
        dict_words[key]['score'] = sum(dict_words[key]['list_score'])
        dict_words[key]['count'] += 1
    # Else create entry
    else:
        elem = {
            'score': value,
            'list_score': [value],
            'count': 1
        }
        dict_words[key] = elem


def get_top_entities_from_a_review(reviews):
    dict_words = {}
    # Look each review
    for review in reviews:
        # Get entities from the review
        dict_aux = from_text_return_dict(review)
        # Insert each entity into location entities dictionary
        for key,value in dict_aux:
            update_score(dict_words,key,value)
    return dict_words
