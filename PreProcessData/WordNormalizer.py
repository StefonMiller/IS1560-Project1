import Classes.Path as Path
from nltk.stem import *

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class WordNormalizer:

    # Stemmer object
    stemmer = None

    def __init__(self):
        # Create stemmer object
        self.stemmer = PorterStemmer()
        return

    def lowercase(self, word):
        # Transform the word uppercase characters into lowercase.
        # Turn word into lowercase with lower function
        word = word.lower()
        return word

    def stem(self, word):
        # Return the stemmed word with Stemmer in Classes package.
        # Stem each word as they come in
        word = self.stemmer.stem(word)
        return word
