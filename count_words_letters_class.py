import string

class count_words_letters:
    '''Analyse the number of words and letters 
    in a text file '''

    punctuation = [punc for punc in string.punctuation]
    whitespace = [spc for spc in string.whitespace]
    
    def remove_punctuation(self, a_string):
        """
        Returns a string
        without punctuation
        """
        new_string = ''
        for char in a_string:
            if char not in punctuation:
                new_string = new_string + char
        return new_string

    def remove_whitespace(self, a_string):
        """
        Returns a string
        without whitespace
        """
        new_string = ''
        for char in a_string:
            if char not in whitespace:
                new_string = new_string + char
        return new_string

    def letters_count(self, text_file):
        """
        Returns a dictionary with all
        the letters present in the text
        and their frequency
        """
        my_text = open(text_file, 'r')
        letters_dict = {}
        for line in my_text.read():
            for char in line:
                char = char.lower()
                if char != '' and char.isalpha():
                    if char not in letters_dict.keys():
                        #The first time a letter is added
                        #as a key with a value 1
                        letters_dict[char] = 1
                    else:
                        #Each time the same letter is
                        #encountered, its value is incremented
                        letters_dict[char] = letters_dict[char] + 1
        my_text.close()
        return letters_dict

    def words_count(self, text_file):
        """
        Returns a dictionary with all
        the words present in the text
        and their frequency
        """
        my_text = open(text_file, 'r')
        words_dict = {}
        for word in my_text.read().split(" "):
            word = word.lower()
            if word != '' and word.isalpha():
                if word not in words_dict:
                    #The first time a word is encountered
                    #it is added as a key with a value of 1
                    words_dict[word] = 1
                else:
                    #Each time the same word is encountered
                    #again, the corresponding value is 
                    #incremented by 1
                    words_dict[word] = words_dict[word] + 1
        my_text.close()
        return words_dict

    def display_letters_count(self, text):
        text_string = remove_whitespace(self.remove_punctuation(text.read().lower()))
        letters = self.letters_count(text_string)
        for k, v in sorted(letters.items()):
            print k, ': ', v

    def display_words_count(self, text):
        text_sample = self.remove_punctuation(text.read().lower().replace('\n', ''))
        words =  self.words_count(text_sample)
        for k, v in sorted(words.items()):
            print k, ': ', v

    def letters_freq(self, text_file):
        """
        Returns a dictionary with all
        the letters and their percentage
        """
        nb_letters = self.letters_count(text_file)
        total = sum(nb_letters.values())
        print 'Total number of letters: ', total
        freq_letters = {}
        for k, v in nb_letters.iteritems():
            freq_letters[k] = round(v * 100. / total, 1) 
        return freq_letters
    
    def words_freq(self, text_file):
        """
        Returns a dictionary with all
        the words and their percentage
        """
        nb_words = self.words_count(text_file)
        total = sum(nb_words.values())
        freq_words = {}
        for k, v in nb_words.iteritems():
            freq_words[k] = round(v * 100. / total, 1) 
        return freq_words


if __name__ == "__main__":
    my_analysis = count_words_letters()
    print my_analysis.words_count('sample.txt')
    print my_analysis.words_freq('sample.txt')
