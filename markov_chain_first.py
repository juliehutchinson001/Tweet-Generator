# '''
# You'll need to write code to do two things:

# Learn a Markov chain from a corpus. You've already written code to find how often a token 
# appears in a corpus (histogram_dictionary), but now you need to find how often a token appears 
# after another token.

# Do a random walk on a Markov chain. This should be pretty simple if you pick a good way to 
# store the Markov chain you learn.

# Make sure to think about what data structures to use to make your code efficient. Both learning 
# the Markov chain and taking a step of the random walk should take time at most linear in 
# the size of the corpus.
# '''
import random
import re
from stochastic_sampling import get_random_word
from histogram_dictionary import Histogram
from markov_words_helper import get_long_words, get_words, get_short_words




if __name__ == "__main__":

    #corpus = 'one fish two fish three fish four fish red fish blue fish'
    clean_data = clean_text(get_words())

    histogram = Histogram(clean_data)
# if you want to return the output of run


    # markov_chn_dict = first_order_markov(get_long_words())
    markov_chn_dict = first_order_markov(clean_data)
    # markov_chn_dict = first_order_markov(get_short_words())


    print(tweet_generator(100, markov_chn_dict))




