import re
import string

def get_long_words():
    dictionary_long_words = ''
    with open('test_corpus.txt') as dictionary_long_file:
        dictionary_long_words += dictionary_long_file.read().lower().replace('\n', ' ')
        remove_punctuation(dictionary_long_words)
        result_long = []

        reg_long_expressions = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", dictionary_long_words)

    remove_punctuation(dictionary_long_words)

def get_words():
    dictionary_words = ''
    with open('short_version.txt') as dictionary_file:
        dictionary_words += dictionary_file.read().lower().replace('\n', ' ')
        remove_punctuation(dictionary_words)
        result = []

        reg_expressions = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", dictionary_words)

    remove_punctuation(dictionary_words)

def get_short_words():
    corpus = 'one fish two fish three fish four fish red fish blue fish'

    return corpus

def remove_punctuation(sample_text):
    remove_text = re.sub('[,.()]', '', remove_text)
    remove_text = re.sub('--', ' ', remove_text)
    remove_text = re.sub(':', ' ', remove_text)
    remove_text = re.sub('/(?<!\S).(?!\S)\s*/', '', remove_text)
    return remove_text