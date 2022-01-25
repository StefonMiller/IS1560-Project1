import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class WordTokenizer:

    # List of tokenized words
    words = []

    def __init__(self, content):
        # Tokenize the input texts.

        # Split content by whitespace
        self.words = content.split()
        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.
        word = ""
        # Check if list of words is empty
        if len(self.words) == 0:
            word = None
        else:
            # Remove first item from words list and return it
            word = self.words.pop(0)
        return word