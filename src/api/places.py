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


if __name__ == '__main__':
    lat, long = geo_coder('Barcelona')
    search(lat, long, 1000, 'Mexican restaurant')
