import operator

from src.api.places import search
from src.nlp.nlp import process_nlp


def _clean_scores_entities(entity_scores, features):
    entity_scores_aux = {}
    for entity in entity_scores.keys():
        if entity in features:
            entity_scores_aux[entity] = entity_scores[entity]
    entity_scores = entity_scores_aux

    for feature in features:
        if feature not in entity_scores:
            entity_scores[feature] = 0.0

    return entity_scores


def _clean_sentences_entities(entity_sentences, features):
    entity_sentences_aux = {}
    for entity in entity_sentences.keys():
        if entity in features:
            entity_sentences_aux[entity] = entity_sentences[entity]
    return entity_sentences_aux


def _get_best_sentence(entity_scores, entity_sentences):
    best_entity = max(entity_scores.items(), key=operator.itemgetter(1))[0]
    if best_entity in entity_sentences:
        return entity_sentences[best_entity]
    else:
        return "", ""


def sort_places(location, necessity, features):
    place_score = {}
    best_sentence = {}
    places = search(location, necessity)
    for place_id in places.keys():
        place = places[place_id]
        reviews = place['reviews']
        entity_scores, entity_sentences = process_nlp(reviews)
        entity_scores = _clean_scores_entities(entity_scores, features)
        entity_sentences = _clean_sentences_entities(entity_sentences, features)

        best_sentence[place_id] = _get_best_sentence(entity_scores, entity_sentences)
        place_score[place_id] = float(sum(entity_scores.values()))

    sorted_places = sorted(place_score.items(), key=operator.itemgetter(1), reverse=True)
    result = []
    for key, value in sorted_places:
        places[key]['score'] = value
        places[key]['person'] = best_sentence[key][0]
        places[key]['sentence'] = best_sentence[key][1]
        result.append(places[key])
    return result[:10]
