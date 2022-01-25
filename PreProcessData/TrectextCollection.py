import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
class TrectextCollection:

    # File pointer
    f = None

    def __init__(self):
        # 1. Open the file in Path.DataTextDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!

        # Assign class variable f to a pointer to the file in Path.DataTextDir, opened in UTF8 encoding
        self.f = open(Path.DataTextDir, encoding="utf8")
        return

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.

        doc = ""
        docNo = ""
        content = ""
        # Read document into a String
        for line in self.f:
            line = line.strip()
            doc = ''.join((doc,'\n', line))
            if line == '</DOC>':
                break
        else:
            # Return None if at end of file
            return None
        docNo = doc[doc.find('<DOCNO>')+len('<DOCNO>'):doc.rfind('</DOCNO>')]
        content = doc[doc.find('<TEXT>')+len('<TEXT>'):doc.rfind('</TEXT>')]
        return [docNo, content]
        
                