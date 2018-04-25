
import random
import string
from stochastic_sampling import get_random_word
from histogram_dictionary import Histogram
from markov_words_helper import remove_punctuation, get_long_words, get_words, get_short_words

#accessing the list of words as string
helper_dictionary_words = get_long_words()
# helper_dictionary_words = get_words()
# helper_dictionary_words = get_short_words()


def first_order_markov(str_words):
    tokens = str_words.split(" ")

    markov_dict = {}
    # any order markov chain, just change the variable to the desired number
    # order = 5
    for index, token_key in enumerate(tokens):
        if index == len(tokens) - 1: break
        # next_token = ' '.join(tokens[index + 1: index + 1 + order])
        if token_key not in markov_dict:
            markov_dict[token_key] = {tokens[index + 1]: 1}
            # any order
            # markov_dict[token_key] = {next_token: 1}
        else:
            next_token = tokens[index + 1]
            if next_token not in markov_dict[token_key]:
                markov_dict[token_key][next_token] = 1
            else:
                markov_dict[token_key][next_token] += 1
    
    return markov_dict

def clean_text (corpus):
    # '''time complexity of this operation: O(k * n * Avg_Word)
    # where k = symbols
    #       n = corpus
    #       Avg_word = length of word

    # result = re.sub(pattern, repl, string, count=0, flags=0);

    # def my_replace(m):
    #     if :
    #     return <replacement variant 1>
    #     return <replacement variant 2>


    # result = re.sub("\w+", my_replace, input)

    # '''

    # symbols = '''!?,;'" -- - :'''
    # clean_string = ''

    # for word in corpus:
    #     for rev_symbol in symbols:
    #         clean_string += word.replace(rev_symbol, '')

    # return word

    # remove_punctuation(word_list)
    # result_list = []

    # items = re.findall("[A-z]+\'?[A-z]*\$[0-9]*", word_list)
    # for item in items:
    #     result_list.append(item)
    # return result_list

    pass

def tweet_generator(order, markov_dict):
    
    final_sentence = ''

    counter = 0
    #convert a dict to a list
    list_of_words = list(markov_dict)

    #returns to me a random word from the previous list
    first_word = random.choice(list_of_words)
    
    #loop to attach my random words to sentence
    while counter != order:

        #call my random_word function from my stochastic sampling
        #and index that to my random word
        random_word_sentence = get_random_word(markov_dict[first_word])
        #append to my sentence string
        final_sentence += random_word_sentence + ' '

        first_word = random_word_sentence

        counter += 1

    return final_sentence.strip()


if __name__ == "__main__":

    #corpus = 'one fish two fish three fish four fish red fish blue fish'
    clean_data = clean_text(get_words())

    histogram = Histogram(clean_data)
# if you want to return the output of run


    # markov_chn_dict = first_order_markov(get_long_words())
    markov_chn_dict = first_order_markov(clean_data)
    # markov_chn_dict = first_order_markov(get_short_words())


    print(tweet_generator(100, markov_chn_dict))




