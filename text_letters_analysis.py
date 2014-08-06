import matplotlib.pyplot as plt
import numpy as np

import count_words_letters_class as cwl


class text_letters_analysis:

    def __init__(self, text):
        self.text = text

    def plot_letters_freq(self, text):
       text_analysis = cwl.count_words_letters(text)
       dict_for_plot = text_analysis.dict_plot_letters(text_analysis.text)
       count, letters = dict_for_plot.get("count"), dict_for_plot.get("letters")
       num_letters = len(count)
       ind = np.arange(num_letters)
       width = 0.75
       x_width = ind + width
       plt.bar(x_width, count, width)
       plt.ylabel('% of occurence')
       plt.xlabel('Letters')
       ticks_pos = [i + 1.1 for i in range(num_letters)]
       plt.xticks(ticks_pos, letters)
       plt.axis([0, 27, 0, 15])
       plt.title('Frequencies of letters in %s' %text)
       return plt.show()

if __name__ == '__main__':
    my_analysis = text_letters_analysis('sample.txt')
    my_analysis.plot_letters_freq(my_analysis.text)
