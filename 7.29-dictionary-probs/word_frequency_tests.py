import unittest
import word_frequency


class TestWordFrequency(unittest.TestCase):
    def test01_sanitize_word(self):
        word = word_frequency.sanitize_word("hello")
        self.assertEqual(word, "hello")

    def test02_sanitize_word(self):
        word = word_frequency.sanitize_word("Hello!")
        self.assertEqual(word, "hello")

    def test03_sanitize_word(self):
        word = word_frequency.sanitize_word("%$^%$")
        self.assertEqual(word, "")

    def test04_count_word(self):
        dct = {"you": 7, "i": 5, "and": 4}
        word_frequency.count_word("you", dct)
        self.assertEqual(dct["you"], 8)
        self.assertEqual(dct["i"], 5)
        self.assertEqual(dct["and"], 4)

    def test05_count_word(self):
        dct = {}
        word_frequency.count_word("you", dct)
        self.assertEqual(dct["you"], 1)
        word_frequency.count_word("i", dct)
        self.assertEqual(dct["i"], 1)

    def test06_count_word(self):
        dct = {"you": 7, "i": 5, "and": 4}
        word_frequency.count_word("", dct)
        self.assertEqual(dct["you"], 7)
        self.assertEqual(dct["i"], 5)
        self.assertEqual(dct["and"], 4)
        self.assertFalse("" in dct)

    def test07_count_words(self):
        dct = word_frequency.count_words("Hello, world!")
        self.assertEqual(dct["hello"], 1)
        self.assertEqual(dct["world"], 1)


if __name__ == "__main__":
    unittest.main()
