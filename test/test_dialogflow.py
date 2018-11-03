import unittest
from src.entities import entities


class TestDialogflow(unittest.TestCase):

    def test_get_entities(self):
        text = 'The place is cozy'
        entities.get_entities(text)
        self.assertEqual('hola','hola')
    


if __name__ == '__main__':
    unittest.main()