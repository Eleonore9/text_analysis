import string
import matplotlib.pyplot as plt
import clean_text_class as ct

class count_words_letters:
    '''Analyse the number of words and letters 
    in a text file '''
    
    alphabet = [l for l in string.ascii_lowercase]
    
    def __init__(self, words, letters):
        self.words = words
        self.letters = letters

    # Methods to count words/letters in a text file
    # Returns a dict with the letter/word as key and
    # the count as value. Ex: {'a': 7, 'f': 3}
    def letters_count(self, letters):
        """
        Returns a dictionary with all
        the letters present in the text
        and their frequency
        """
        l = sorted(letters)
        letters_dict = {a:l.count(a) for a in alphabet}
        return letters_dict

    def words_count(self, words):
        """
        Returns a dictionary with all
        the words present in the text
        and their frequency
        """
        l = sorted(words)
        words_dict = {w:l.count(w) for w in l}
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
    test = ct.clean_text('books/test2.txt')
    my_text = test.remove_punctuation(test.remove_chapters(test.remove_metadata(test.text)))
    my_words = test.whole_text_words(my_text)
    my_letters = test.text_letters(my_text)
    cwl = count_words_letters(my_words, my_letters)
    print cwl.words_count(cwl.words)
    #d = my_analysis.dict_plot_letters(my_analysis.text)
    #my_analysis.plot_letters(d)
