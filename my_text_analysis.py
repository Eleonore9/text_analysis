import count_words_letters_class as cwl
import matplotlib.pyplot as plt

CWL = cwl.count_words_letters()

def dict_plot_letters(input_txt_file):
    """
    Returns a dict with a list of letters and their
    corresponding frequencies. It is needed to plot
    with Matplotlib. Matplotlib needs a list of 
    values to plot. 
    """
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
    print 'nb of letters: ', len(dict_plot['count'])
    plt.plot(dict_plot.get('count'))
    plt.show()
    #plt.title("Letters content in a text (in %)")
    #plt.xlabel("Letters")
    #plt.ylabel("%")
    #plt.hist(dict_plot['count'], range(len(dict_plot['count'])))
    #return plt.show()

if __name__ == "__main__":
    data_plt = list_for_plot_letters('sample.txt')
    plot_word_letters(data_plt)
