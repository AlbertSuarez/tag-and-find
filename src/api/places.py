import requests

from src.api.here import geo_coder

from src import *


def search(latitude, longitude, radius, keyword):
    payload = {
        'key': MAPS_API_KEY,
        'location': '{lat},{lng}'.format(lat=latitude, lng=longitude),
        'radius': radius,
        'keyword': keyword
    }
    response = requests.get(MAPS_PLACES_URL, params=payload).json()
    id_array = []
    for res in response['results']:
        id_array.append(res['id'])
    return id_array


def get_place(place_id):
    payload = {
        'key': MAPS_API_KEY,
        'placeid': place_id
    }
    response = requests.get(MAPS_PLACE_DETAILS_URL, params=payload).json()
    result = response['result']
    return {
        'name': result['name'],
        'url': result['url'],
        'rating': result['rating'],
        'address': result['formatted_address'],
        'price_level': result['price_level'],
        'photo': 'l',
        'types': result['types'],
        'reviews': [review['text'] for review in result['reviews']]
    }


if __name__ == '__main__':
    lat, long = geo_coder('Barcelona')
    search(lat, long, 1000, 'Mexican restaurant')
