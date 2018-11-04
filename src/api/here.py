import requests

from src import *


# noinspection PyBroadException
def geo_coder(search_text):
    """
    Get latitude and longitude given a search text
    :param search_text: search text
    :return: latitude and longitude
    """
    payload = {
        'app_id': HERE_APP_ID,
        'app_code': HERE_APP_CODE,
        'searchtext': search_text
    }
    response = requests.get(HERE_GEO_CODER_URL, params=payload)
    response_json = response.json()
    try:
        latitude = response_json['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
        longitude = response_json['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
        return latitude, longitude
    except Exception:
        return 53.0759172, 8.8069419  # a static coordinates for avoiding errors
