import operator

from src.api.places import search
from src.nlp.nlp import process_nlp


def _clean_entities(entity_scores, features):
    for entity in entity_scores.keys():
        if entity not in features:
            entity_scores.pop(entity, None)

    for feature in features:
        if feature not in entity_scores:
            entity_scores[feature] = 0.0

    return entity_scores


def sort_places(location, necessity, features):
    place_score = {}
    places = search(location, necessity)
    for place_id in places.keys():
        place = places[place_id]
        reviews = place['reviews']
        entity_scores = process_nlp(reviews)
        entity_scores = _clean_entities(entity_scores, features)
        place_score[place_id] = float(sum(entity_scores.values()))

    sorted_places = sorted(place_score.items(), key=operator.itemgetter(1), reverse=True)
    result = []
    for key, value in sorted_places:
        places[key]['score'] = value
        result.append(places[key])
    return result
