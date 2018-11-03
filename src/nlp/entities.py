from src.nlp.synonims import DICT_WORD

def get_entities(text_list):
    response = []
    for element in text_list:
        if element in DICT_WORD:
            response.append(dict_word[element])
    return response