import unittest
from src.nlp import nlp
from textblob import TextBlob

class TestNLP(unittest.TestCase):

    def test_divide_sentences(self):
        text_sample = 'This place is cozy and quiet. But it is not very clean.'
        text_b = TextBlob(text_sample)
        sentences = nlp.get_sentences(text_b)
        self.assertEqual(len(sentences), 2)

    def test_get_dictionary(self):
        text_sample = 'This place is cozy and quiet. But it is not very clean.'
        dict_word = nlp.from_text_return_dict(text_sample)
        self.assertEqual('hola','hola')
    


if __name__ == '__main__':
    unittest.main()