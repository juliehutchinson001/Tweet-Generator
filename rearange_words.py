import random
import sys

def rearange_words(words):
    #Debugging purposes
    if len(words) == 0:
        raise ValueError('Input a valid list of words')
    #initialize my variables variables
    rand_indexes = []
    final_words_rand = " " #space to concatenate my random words

    #define/describe other variables --different than 0 or ""
    array_word_length = len(words)
    rand_indx_len = len(rand_indexes)

    #loop the random numbers until rand_indexes is full
    while rand_indx_len != array_word_length:
        #store random number in variable called rand_index
        rand_index = random.randint(0, array_word_length - 1)
        #contition the appending of random numbers to rand_index
        if rand_index in rand_indexes:
            continue
        #to generate an array of non-repeating indexes
        else:
            rand_indexes.append(rand_index)
        #update my length of random indexes
        rand_indx_len = len(rand_indexes)

    #loop the random indexes to randomize the array of strings    
    for index in rand_indexes:
        final_words_rand += words[index] + ' '

    #return the final string of words
    return final_words_rand.strip()


def main():
    #gather command-line arguments to the execution of the script
    listed_words = sys.argv[1:]
    #return to the command-line
    return rearange_words(listed_words)

if __name__ == '__main__':
    #invoke my main function
    print(main())