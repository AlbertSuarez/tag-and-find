from textblob import TextBlob
from src.nlp import entities


def _update_score(dict_words, entity, score, sentence, person):
    """
    Update global dictionary of scores
    :param dict_words: dict words
    :param entity: entity
    :param score: score
    :param sentence: sentence
    :param person: person
    :return: `dict_word` updated
    """
    if entity in dict_words:
        dict_words[entity]['count'] += 1
        dict_words[entity]['total_score'] += score
        if score >= dict_words[entity]['max_score']:
            dict_words[entity]['max_score'] = score
            dict_words[entity]['sentence'] = sentence
            dict_words[entity]['person'] = person
    else:
        dict_words[entity] = {
            'total_score': score,
            'count': 1,
            'max_score': score,
            'sentence': sentence,
            'person': person
        }


def _get_sentiment(text):
    """
    Get sentiment score and best sentence given a review
    :param text: review text
    :return: score and best sentence
    """
    # Analyse text using NLP
    text_b = TextBlob(text)
    # Split in sentences
    sentences = text_b.sentences
    result_score = {}
    result_sentence = {}
    for sentence in sentences:
        # Get entities
        entity_list = entities.get_entities(sentence.words)
        # Assign sentiment score
        sent = sentence.sentiment.polarity
        # Assign sentiment to the entities
        for entity in entity_list:
            if entity not in result_score:
                result_score[entity] = sent
                result_sentence[entity] = str(sentence)
            else:
                # If we have a duplicate entity in the same review, we'll keep the greater score
                if sent >= result_score[entity]:
                    result_sentence[entity] = str(sentence)
                result_score[entity] = max(sent, result_score[entity])
    return result_score, result_sentence


def process_nlp(reviews):
    """
    Process all the reviews using NLP
    :param reviews: list of reviews
    :return: a list of entities and their scores and best sentences
    """
    result = {}
    # Look each review
    for person, review in reviews:
        # Get entities from the review
        dict_scores, dict_sentences = _get_sentiment(review)
        # Insert each entity into location entities dictionary
        for entity in dict_scores.keys():
            _update_score(result, entity, dict_scores[entity], dict_sentences[entity], person)

    # Calculate means
    entity_scores = {}
    for key in result.keys():
        entity_scores[key] = result[key]['total_score']/result[key]['count']

    # Get best sentences
    sentences = {}
    for key in result.keys():
        sentences[key] = (result[key]['person'], result[key]['sentence'])

    return entity_scores, sentences
