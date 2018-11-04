import uuid
import requests

from src.api.here import geo_coder

from src import *


def _get_ids(latitude, longitude, keyword):
    """
    Retrieve place identifier given some parameters
    :param latitude: latitude
    :param longitude: longitude
    :param keyword: key query
    :return: array of place ids
    """
    payload = {
        'key': MAPS_API_KEY,
        'location': '{lat},{lng}'.format(lat=latitude, lng=longitude),
        'rankby': 'distance',
        'keyword': keyword,
    }
    response = requests.get(MAPS_PLACES_URL, params=payload).json()
    return [res['place_id'] for res in response['results']]


def _get_place(place_id):
    """
    Retrieve place information given its id
    :param place_id: place identifier
    :return: place information
    """
    payload = {
        'key': MAPS_API_KEY,
        'placeid': place_id
    }
    result = requests.get(MAPS_PLACE_DETAILS_URL, params=payload).json()['result']

    photo_path = ''
    if 'photos' in result:
        for photo in result['photos']:
            photo_path = get_photo(photo['photo_reference'])
            break

    return {
        'name': result['name'],
        'url': result['url'],
        'rating': None if 'rating' not in result else result['rating'],
        'address': None if 'formatted_address' not in result else result['formatted_address'],
        'price_level': None if 'price_level' not in result else result['price_level'],
        'photo': photo_path,
        'types': [] if 'types' not in result else result['types'],
        'reviews': [] if 'reviews' not in result else [(review['author_name'], review['text']) for review in result['reviews']]
    }


def get_photo(photo_reference):
    """
    Retrieve photo given its reference
    :param photo_reference: photo reference
    :return: photo path
    """
    payload = {
        'key': MAPS_API_KEY,
        'photoreference': photo_reference,
        'maxheight': 256,
        'maxweight': 512
    }
    response = requests.get(MAPS_PHOTO_URL, params=payload)
    image_file_name = '{}.jpg'.format(uuid.uuid4())
    image_path = 'src/static/images/{}'.format(image_file_name)
    with open(image_path, 'wb') as image_file:
        image_file.write(response.content)
    return "/static/images/{}".format(image_file_name)


def search(location, necessity):
    """
    Search places given a location and a necessity
    :param location: location
    :param necessity: necessity
    :return: array of places
    """
    lat, long = geo_coder(location)
    places_id = _get_ids(lat, long, necessity)
    return {place_id: _get_place(place_id) for place_id in places_id}
