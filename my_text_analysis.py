import count_words_letters_class as cwl
import matplotlib.pyplot as plt

CWL = cwl.count_words_letters()

def list_for_plot_letters(input_txt_file):
    letters = CWL.letters_freq(input_txt_file)
    dict_letters = {
            'letters': [],
            'count': []
    }
    for k, v in letters.iteritems():
        dict_letters['count'].append(v)
        dict_letters['letters'].append(k)
    return dict_letters

def plot_word_letters(dict_plot):
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.bar(dict_plot['letters'], dict_plot['count'], width=100)
    return plt.show()

if __name__ == "__main__":
#count words and letters for two sample texts:
    data_plt = list_for_plot_letters('sample.txt')
    plot_word_letters(data_plt)
    #print test.words_freq('sample.txt')
