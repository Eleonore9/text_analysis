import string
import re

class clean_text:
    '''Deal with metadata for books
    from Gutenberg project. Clean the
    text'''

    def __init__(self, text):
        self.text = text
        self.punctuation = [punc for punc in string.punctuation]
        self.whitespace = [spc for spc in string.whitespace]
        self.metadata = {}

        ## Helper to take care of the metadata:
    def store_metadata(self, text):
        ''' Build a dictionary with metadata from
        the top of the text file'''
        text_file = open(text, 'r')
        meta =  text_file.read(265)
        title, author, language = "", "", ""
        try:
            t = re.search("Title: [A-Za-z'\t' .]+", meta)
            a = re.search("Author: [A-Za-z'\t' .]+", meta)
            l = re.search("Language: [A-Za-z'\t' .]+", meta)
            title += t.group(0)
            author += a.group(0)
            language += l.group(0)
        except:
            pass
        metadata = {"title": title.replace("Title: ", ""),
                    "author": author.replace("Author: ", ""),
                    "language": language.replace("Language: ", "")}
        text_file.close()
        return metadata

        ## Helpers to actually clean the whole text:
        ##First remove the the metadata
    def remove_metadata(self, text):
        text_file = open(text, 'r')
        text_file.read(265)
        clean_text = text_file.read().strip()
        text_file.close()
        return clean_text
        
    def remove_punctuation_from_str(self, a_string):
        """Returns a string without 
        punctuation"""
        new_string = ''
        for char in a_string:
            if char not in self.punctuation:
                new_string = new_string + char
        return new_string

    def remove_whitespace_from_str(self, a_string):
        """Returns a string
        without whitespace"""
        new_string = ''
        for char in a_string:
            if char not in self.whitespace:
                new_string = new_string + char
        return new_string



if __name__ == "__main__":
    clean_test = clean_text('books/test.txt')
    #clean_test.store_metadata(clean_test.text)
    print clean_test.remove_metadata(clean_test.text)
