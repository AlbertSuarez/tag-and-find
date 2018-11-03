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


if __name__ == '__main__':
    lat, long = geo_coder('Barcelona')
    search('Mexican Restaurants', 5000, lat, long)
