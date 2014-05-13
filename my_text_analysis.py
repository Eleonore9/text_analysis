import count_words_letters as cwl

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


if __name__ == "__main__":
#count words and letters for two sample texts:
    print list_for_plot_letters('sample.txt')
    #print test.words_freq('sample.txt')
