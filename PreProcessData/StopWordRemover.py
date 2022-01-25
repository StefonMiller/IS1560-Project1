import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class StopWordRemover:

    stopwords = None

    def __init__(self):
        # Load and store the stop words from the fileinputstream with appropriate data structure.
        # NT: address of stopword.txt is Path.StopwordDir.

        # Initialize stopwords data structure. Using a set for fast existence checking
        self.stopwords = set()

        # Open stopwords file and read each line into the set
        with open(Path.StopwordDir, encoding="utf8") as f:
            for line in f:
                self.stopwords.add(line)
        return

    def isStopword(self, word):
        # Return true if the input word is a stopword, or false if not.

        # Check if word is in the set, return t/f depending on result
        if word in self.stopwords:
            return True
        else:
            return False
