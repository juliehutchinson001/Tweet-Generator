from helper_dictionary import main
import random
import sys

#accessing the list of words as string
str_dictionary_words = main()

#splitting the list of words by new line to create an array
arr_dictionary_words = str_dictionary_words.split('\n')

#finding the length of the words array --347k aprox.
len_arr_dictionary = len(arr_dictionary_words) - 1


# sys.argv = [name_of_file, next_argument, next_argument....]
words_num = int(sys.argv[1])
str_words = ""
arr_rand_indexes = []
# same_index_picked = 0 # speed optimization testing

#selecting random numbers for my random array of indexes
while len(arr_rand_indexes) != words_num:
    #do random.randint for integer numbers
    rand_int = random.randint(0, len_arr_dictionary)
    
    #condition non-repeating indexes:
    if rand_int not in arr_rand_indexes:
        #append the random #s to array of indexes
        arr_rand_indexes.append(rand_int)
    else:
        # same_index_picked += 1 # Chances of getting a repeated random index
        continue


#using the random indexes, select the newly random words
for dic_words_index in arr_rand_indexes:
    str_words +=  arr_dictionary_words[dic_words_index] + " "

# Testing Print outs:

# print(same_index_picked)
# print("words_num: ", words_num)
# print("arr_rand_indexes: ", arr_rand_indexes)
# print("random words: ", str_words)