import count_words_letters as cwl

if __name__ == "__main__":
#count words and letters for two sample texts:
    test = cwl.count_words_letters()
    print test.letters_freq('sample.txt')
    print test.words_freq('sample.txt')
