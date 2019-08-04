from markov_chain_first import first_order_markov # , tweet_generator
from histogram_dictionary import get_histogram
from flask import Flask, request, render_template, redirect
import random
import sys
import re
import string

app = Flask(__name__)
app.config['DEBUG'] = True

def get_random_word(histogram):

    # if the lenght of my histogram dictionary
    if len(histogram) == 0:
        return None

    # variable for measuring the probability of a word (float)
    cummu_wght = 0

    #calling a random number from 0 to 1 (float)
    random_num = random.random()

    #iterating through my histogram with the item properties
    for key, value in histogram.items():

        #calculating my percentage of a word based on the value
        type_percentage = value / sum(histogram.values())

        cummu_wght += type_percentage

        #if my random number is less than the weight of a word, don't add it
        if random_num <= cummu_wght:
            remove_more = re.sub(",", '', key)
            remove_even_more = re.sub("'", ' ', remove_more)

            return remove_even_more.strip()
            #import pdb; pdb.set_trace() # debugging



def test_get_random_word(repetitions, histogram):

    list_of_words = []

    for _ in range(repetitions):

        rand_word = get_random_word(histogram)

        list_of_words.append(rand_word)

    histogram = get_histogram(list_of_words)

    return histogram

def tweet_generator(order, markov_dict):

    final_sentence = ''

    counter = 0
    #convert a dict to a list
    list_of_words = list(markov_dict)

    #returns to me a random word from the previous list
    first_word = random.choice(list_of_words)

    #loop to attach my random words to sentence
    while counter != order:

        # index random_word function to my random word
        random_word_sentence = get_random_word(markov_dict[first_word])

        first_word = random_word_sentence

        # append to my sentence string
        final_sentence += random_word_sentence

        sentence = ''.join(final_sentence)

        counter += 1

    remove_more = re.sub(",", '', sentence)
    remove_even_more = re.sub("'", ' ', remove_more)
    # print(remove_even_more)
    # print("test: " + sentence[0])

    return remove_even_more.strip()

@app.route('/', methods=['GET', 'POST'])
def main():
    try:
        with open('test_corpus.txt') as file:
            raw_data = file.read().lower()
    except:
        print('Please enter a valid file name')
        return

    if request.method == 'POST':

        clean_data = get_clean_data(raw_data)

        histogram = get_histogram(clean_data)

        try:

            sentence_length = int(request.form['sentence_length'])
        except:
            sentence_length = 7
            # raise ValueError('please enter a number')
            # return
        if sentence_length > 25:
            raise ValueError('Please enter a number less than 25')


        # test_result = test_get_random_word(sentence_length, histogram)

    # Turns dictionary into string so that it can be displayed in the browser
        # remove period and spaces in the starting token
        starting_word = random.choice(starting_words)[1:].strip()
        end_token = random.choice(ending_words)

        rand_sentence = sentence_generator(sentence_length, histogram, starting_word)
        rand_sentence += ' ' + end_token
        return render_template('display_sentence.html',
                                rand_sentence=rand_sentence)
    else:
        return render_template('show_form.html')

def get_start_end_tokens(text, pattern):
    words = re.findall(pattern, text)
    clean_words = [word.strip() for word in words]
    return clean_words

if __name__=='__main__':
    app.run()