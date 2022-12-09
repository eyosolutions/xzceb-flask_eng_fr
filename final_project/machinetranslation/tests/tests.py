import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench('None'), '')
        self.assertNotEqual(englishToFrench(0), 0)
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchToEnglish('None'), '')
        self.assertNotEqual(frenchToEnglish(0), 0)
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()