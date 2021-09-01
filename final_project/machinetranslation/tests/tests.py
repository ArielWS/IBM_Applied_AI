import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    def test2(self):
        self.assertNotEqual(englishToFrench('Hello'),'Ennui')


class TestFrenchToEnglish(unittest.TestCase):
    def test3(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    def test4(self):
        self.assertNotEqual(frenchToEnglish('Bonjour'),'Backflip')

unittest.main()
#Ariel Spilkin wrote this