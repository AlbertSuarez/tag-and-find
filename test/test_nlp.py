import unittest
from src.nlp import nlp
from textblob import TextBlob

class TestNLP(unittest.TestCase):

    def test_divide_sentences(self):


        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()import unittest