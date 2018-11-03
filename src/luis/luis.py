
from src import *
from src.util import request

def get_entities(query):
    """
    Get intent from LUIS
    :param query: query
    :return: LUIS answer
    """
    headers = {
        'Ocp-Apim-Subscription-Key': LUIS_SUBSCRIPTION_KEY,
    }
    params = {
        'q': query,
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }
    try:
        url = 'https://{}/luis/v2.0/apps/{}'.format(LUIS_SERVER, LUIS_ID)
        response_data = request.execute(method='GET', url=url, headers=headers, params=params)
        return analyze_response(response_data)
    except Exception as e:
        print(e.message)


def analyze_response(response_data):
    """
    Analyze LUIS response
    :param response_data: response data
    :return: response analyzed
    """
    try:
        # Retrieve intent
        entities = response_data['topScoringIntent']['entities']
        return entities

    except Exception as e:
        # Log error and return default error message
        log.error(e)
        return error.get_message()
