from textblob import TextBlob
from src.nlp import entities


def _update_score(dict_words, entity, score):
    if entity in dict_words:
        dict_words[entity]['count'] += 1
        dict_words[entity]['total_score'] += score
    else:
        dict_words[entity] = {'total_score': score, 'count': 1}


def _get_sentiment(text):
    # Analyse text using NLP
    text_b = TextBlob(text)
    # Split in sentences
    sentences = text_b.sentences
    result = {}
    for sentence in sentences:
        # Get entities
        entity_list = entities.get_entities(sentence.words)
        # Assign sentiment score
        sent = sentence.sentiment.polarity
        # Assign sentiment to the entities
        for entity in entity_list:
            if entity not in result:
                result[entity] = sent
            else:
                # If we have a duplicate entity in the same review, we'll keep the greater score
                result[entity] = max(sent, result[entity])
    return result


def process_nlp(reviews):
    result = {}
    # Look each review
    for review in reviews:
        # Get entities from the review
        dict_aux = _get_sentiment(review)
        # Insert each entity into location entities dictionary
        for entity in dict_aux.keys():
            _update_score(result, entity, dict_aux[entity])

    # Calculate means
    entity_scores = {}
    for key in result.keys():
        entity_scores[key] = result[key]['total_score']/result[key]['count']
    return entity_scores
