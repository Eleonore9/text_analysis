import string
import matplotlib.pyplot as plt

class count_words_letters:
    '''Analyse the number of words and letters 
    in a text file '''
    
    def __init__(self, text):
        self.text = text
        self.punctuation = [punc for punc in string.punctuation]
        self.whitespace = [spc for spc in string.whitespace]
        self.letters_dict = {letter:0 for letter in string.ascii_lowercase}

    def remove_punctuation(self, a_string):
        """
        Returns a string
        without punctuation
        """
        new_string = ''
        for char in a_string:
            if char not in self.punctuation:
                new_string = new_string + char
        return new_string

    def remove_whitespace(self, a_string):
        """
        Returns a string
        without whitespace
        """
        new_string = ''
        for char in a_string:
            if char not in self.whitespace:
                new_string = new_string + char
        return new_string
    
    # Methods to count words/letters in a text file
    # Returns a dict with the letter/word as key and
    # the count as value. Ex: {'a': 7, 'f': 3}
    def letters_count(self, text):
        """
        Returns a dictionary with all
        the letters present in the text
        and their frequency
        """
        my_text = open(text, 'r')
        for line in my_text.read():
            for char in line:
                char = char.lower()
                if char != '' and char.isalpha():
                    self.letters_dict[char] += 1
        my_text.close()
        print 'DICT COUNTS: ', self.letters_dict
        return self.letters_dict

    def words_count(self, text):
        """
        Returns a dictionary with all
        the words present in the text
        and their frequency
        """
        my_text = open(text, 'r')
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

    # Methods to display the counts in a nice way.
    # It prints out the letters/words with their count.
    def display_letters_count(self, text):
        letters = self.letters_count(text)
        for k, v in sorted(letters.items()):
            print k, ': ', v

    def display_words_count(self, text):
        words =  self.words_count(text)
        for k, v in sorted(words.items()):
            print k, ': ', v

    # Methods to retrieve words/letters frequencies in a text file.
    # They return a dictionary containing the letters/words and 
    # their frequencies.
    def letters_freq(self, text):
        """
        Returns a dictionary with all
        the letters and their percentage
        """
        nb_letters = self.letters_count(text)
        total = sum(nb_letters.values())
        print 'Total number of letters: ', total
        freq_letters = {}
        for k, v in nb_letters.iteritems():
            freq_letters[k] = round(v * 100. / total, 1) 
        return freq_letters
    
    def words_freq(self, text):
        """
        Returns a dictionary with all
        the words and their percentage
        """
        nb_words = self.words_count(text)
        total = sum(nb_words.values())
        freq_words = {}
        for k, v in nb_words.iteritems():
            freq_words[k] = round(v * 100. / total, 1) 
        return freq_words

    # Method to output the letters frequencies differently.
    # It returns a dictionary containing two key/value pairs.
    # One lists the letters/words, the other one the frequencies.
    def dict_plot_letters(self, text):
        """
        Returns a dict with a list of letters and their
        corresponding frequencies. It is needed to plot
        with Matplotlib. Matplotlib needs a list of 
        values to plot. 
        """
        letters = self.letters_freq(text)
        print '1st FREQ DICT: ', letters
        dict_letters = {
                'letters': [],
                'count': []
        }
        for k, v in sorted(letters.iteritems()):
            dict_letters['count'].append(v)
            dict_letters['letters'].append(k)
        print '2nd FREQ DICT: ', dict_letters
        return dict_letters

    def plot_letters(self, dict_plot):
        """
        Trying to plot the frequencies
        with matplotlib.
        """
        print 'nb of letters: ', len(dict_plot['count'])
        #plt.plot(dict_plot.get('count'))
        #plt.show()
        plt.title("Letters content in a text (in %)")
        plt.xlabel("Letters")
        plt.ylabel("%")
        plt.hist(dict_plot['count'], range(len(dict_plot['count'])))
        return plt.show()

if __name__ == "__main__":
    my_analysis = count_words_letters('books/sample.txt')
    d = my_analysis.dict_plot_letters(my_analysis.text)
    my_analysis.plot_letters(d)
