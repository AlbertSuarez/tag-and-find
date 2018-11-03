import requests

from src.api.here import geo_coder

from src import *


def search(query, radius, latitude, longitude):
    payload = {
        'key': MAPS_API_KEY,
        'input': query,
        'inputtype': 'textquery',
        'locationbias': 'circle:{radius}@{lat},{lng}'.format(radius=radius, lat=latitude, lng=longitude)
    }
    response = requests.get(MAPS_PLACES_URL, params=payload).json()
    print(response)


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
    search('Mexican Restaurants', 5000, lat, long)
