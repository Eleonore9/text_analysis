import string
import matplotlib.pyplot as plt
import clean_text_class as ct

class count_words_letters:
    '''Analyse the number of words and letters 
    in a text file '''
    
    
    def __init__(self, words, letters):
        self.words = words
        self.letters = letters
        self.alphabet = [l for l in string.ascii_lowercase]

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
        letters_dict = {a:l.count(a) for a in self.alphabet}
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

    # Methods to retrieve letters frequencies and plot them.
    def letters_freq(self, letters_dict):
        """
        Returns a dictionary with all
        the letters and their percentage
        """
        total = sum(letters_dict.values())
        freq_letters = {k:round(v *100./total, 1) for k, v in letters_dict.items()}
        return freq_letters
    
    def plot_letters(self, dict_freq):
        """
        Trying to plot the frequencies
        with matplotlib.
        """
        d = sorted(dict_freq.iteritems())
        letters, freqs = tuple(x[0] for x in d), tuple(x[1] for x in d)
        print list(freqs)
        plt.title("Letters content (in %)")
        plt.xlabel("Letters")
        plt.ylabel("%")
        plt.plot(range(1, len(freqs) + 1), list(freqs))
        plt.axis([1, 26, 0.0, 12.0])
        plt.grid(True)
        return plt.show()

if __name__ == "__main__":
    test = ct.clean_text('books/test2.txt')
    my_text = test.remove_punctuation(test.remove_chapters(test.remove_metadata(test.text)))
    my_words = test.whole_text_words(my_text)
    my_letters = test.text_letters(my_text)
    cwl = count_words_letters(my_words, my_letters)
    l_freq = cwl.letters_freq(cwl.letters_count(cwl.letters))
    print l_freq
    cwl.plot_letters(l_freq)
