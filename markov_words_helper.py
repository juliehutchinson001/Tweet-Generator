def get_long_words():
    dictionary_long_words = ''
    with open('test_corpus.txt') as dictionary_long_file:
        dictionary_long_words += dictionary_long_file.read().replace('\n', ' ')

    return dictionary_long_words

def get_words():
    dictionary_words = ''
    with open('short_version.txt') as dictionary_file:
        dictionary_words += dictionary_file.read().replace('\n', ' ')

    return dictionary_words

