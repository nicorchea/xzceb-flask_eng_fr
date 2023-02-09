import unittest
from translator import french_to_english, english_to_french

class TranslationTests(unittest.TestCase):
    def test_french_to_english_nullInput(self):
        self.assertRaises(TypeError, french_to_english, None)
        
    def test_english_to_french_nullInput(self):
        self.assertRaises(TypeError, english_to_french, None)
        
    def test_french_to_english_wordTranslation(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        
    def test_english_to_french_wordTranslation(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

if __name__ == '__main__':
    unittest.main()