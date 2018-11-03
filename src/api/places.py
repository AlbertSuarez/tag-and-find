import uuid
import requests

from src.api.here import geo_coder

from src import *


def get_ids(latitude, longitude, radius, keyword):
    """
    Retrieve place identifier given some parameters
    :param latitude: latitude
    :param longitude: longitude
    :param radius: radius
    :param keyword: key query
    :return: array of place ids
    """
    payload = {
        'key': MAPS_API_KEY,
        'location': '{lat},{lng}'.format(lat=latitude, lng=longitude),
        'radius': radius,
        'keyword': keyword
    }
    response = requests.get(MAPS_PLACES_URL, params=payload).json()
    id_array = []
    for res in response['results']:
        id_array.append(res['place_id'])
    return id_array


def get_photo(photo_reference):
    """
    Retrieve photo given its reference
    :param photo_reference: photo reference
    :return: photo path
    """
    payload = {
        'key': MAPS_API_KEY,
        'photoreference': photo_reference,
        'maxheight': 256
    }
    response = requests.get(MAPS_PHOTO_URL, params=payload)
    image_path = 'src/images/{}.jpg'.format(uuid.uuid4())
    with open(image_path, 'wb') as image_file:
        image_file.write(response.content)

    return image_path


def get_place(place_id):
    payload = {
        'key': MAPS_API_KEY,
        'placeid': place_id
    }
    result = requests.get(MAPS_PLACE_DETAILS_URL, params=payload).json()['result']
    return {
        'name': result['name'],
        'url': result['url'],
        'rating': None if 'rating' not in result else result['rating'],
        'address': None if 'formatted_address' not in result else result['formatted_address'],
        'price_level': None if 'price_level' not in result else result['price_level'],
        'photo': None if 'photos' not in result else [photo['photo_reference'] for photo in result['photos']],
        'types': [] if 'types' not in result else result['types'],
        'reviews': [] if 'reviews' not in result else [review['text'] for review in result['reviews']]
    }


def search(place, necessity):
    lat, long = geo_coder(place)
    places_id = get_ids(lat, long, 1000, necessity)
    return [get_place(place_id) for place_id in places_id]


if __name__ == '__main__':
    r = search('Barcelona', 'Mexican restaurant')
    print(r)
