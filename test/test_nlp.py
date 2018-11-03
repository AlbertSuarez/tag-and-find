import unittest
from src.nlp import nlp
from textblob import TextBlob

class TestNLP(unittest.TestCase):

    def test_divide_sentences(self):
        text_sample = 'This place is cozy and quiet. But it is not very clean.'
        text_b = TextBlob(text_sample)
        sentences = nlp.get_sentences(text_b)
        self.assertEqual(len(sentences), 2)

    def test_get_adjectives(self):
        text_sample = 'This place is cozy and quiet'
        text_b = TextBlob(text_sample)
        adj = nlp.get_topic(text_b)
        arr = ['cozy', 'quiet']
        self.assertEqual(adj,arr)

    def test_get_adjectives_from_sentence(self):
        text_sample = 'This place is cozy and quiet. But it is not very clean.'
        text_b = TextBlob(text_sample)
        adj = nlp.get_topic(text_b)
        arr = ['cozy', 'quiet','clean']
        self.assertEqual(adj,arr)

    def get_topic_and_adjective(self):
        text_sample = 'This place is cozy and quiet'
        text_b = TextBlob(text_sample)
    


if __name__ == '__main__':
    unittest.main()