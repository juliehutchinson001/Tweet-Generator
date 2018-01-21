'''
Visualizing histogram
original_str = 'one fish two fish three fish four fish'
dict_histogram_of_original_str = {one: 1, fish: 4, two: 1, three: 1, four: 1}
'''

def histogram(str_words: str) -> dict:
    # initialize my variables
    dict_histogram = {}
    
    # receive a string and split it to create an array
    arr_words = str_words.split()

    # iterate array
    for word_indexed in arr_words:
        # condition plus one each repeated word
        if word_indexed not in dict_histogram:
            # add new word to dictionary
            dict_histogram[word_indexed] = 1
        else:
            # increment counter for words that already exist
            dict_histogram[word_indexed] += 1
            
    # call unique_words function to count the total unique words
    print(unique_words(dict_histogram))

    #return dictionary
    return dict_histogram


def unique_words(d_histogram: dict) -> int:
    # #counter tracker for unique words
    # count_values = 0
    # #loop the content of the dictionary
    # for key, value in d_histogram.items():
    #     #count the types in histogram
    #     count_values += 1
    return len(d_histogram) 
    
    #return count_values

def frequency(find_word: str, wrd_histogram: dict) -> int:
    #loop the content of the dictionary to find_word as a dict key
    # for key, value in wrd_histogram.items():
    #     #search the keyword within the histogram dictionary
    #     if key == find_word:
    #         # When find_word found return the value
    #         return value
            
    return wrd_histogram[find_word] if find_word in wrd_histogram else 0



def main():
    #sample string
    str_words = 'one fish two fish three fish four fish'
    
    #calling function histogram with sample string
    main_functionality = histogram(str_words)

    #calling function frequency with histogram output as dict argument
    histogram_freq = frequency('fish', main_functionality)

    print(histogram_freq)

if __name__ == "__main__":
    main()