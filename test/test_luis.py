import unittest
from src.luis import luis


class TestLuis(unittest.TestCase):

    def test_get_entities(self):
        text = 'The place is cozy'
        entities = luis.get_entities(text)
        self.assertEqual('hola','hola')
    


if __name__ == '__main__':
    unittest.main()