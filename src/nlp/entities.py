from src.nlp.synonims import DICT_WORD


def get_entities(text_list):
    """
    Retrieve entities given a text list
    :param text_list: text list
    :return: array of entities
    """
    response = []
    for element in text_list:
        if element in DICT_WORD and DICT_WORD[element] not in response:
            response.append(DICT_WORD[element])
    return response
