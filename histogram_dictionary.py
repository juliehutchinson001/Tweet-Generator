'''
Visualizing histograms
original_str = 'one fish two fish three fish four fish'
dict_histogram_of_original_str = {one: 1, fish: 4, two: 1, three: 1, four: 1}

>* A frequency() function that takes a word and histogram argument and returns the number of times that 
word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will 
return the integer 20.
'''

def histogram(str_words: str) -> dict:
    #TODO: initialize my variables
    dict_histogram = {}
    
    #TODO: receive a string and split it to create an array
    arr_words = str_words.split()

    #TODO: iterate array
    for word_indexed in arr_words:
        #TODO: condition plus one each repeated word
        if word_indexed not in dict_histogram:
            #TODO: add new word to dictionary
            dict_histogram[word_indexed] = 1
        else:
            #TODO: increment counter for words that already exist
            dict_histogram[word_indexed] += 1
            
    #TODO: call unique_words function to count the total unique words
    print(unique_words(dict_histogram))

    #return dictionary
    return dict_histogram


def unique_words(d_histogram: dict) -> int:
    #counter tracker for unique words
    count_values = 0

    #loop the content of the dictionary
    for key, value in d_histogram.items():
        #condition the values of histogram to obtain non-repeating ones
        if value == 1:
            count_values += value
            
    #print(count_values)
    
    return count_values

def frequency(find_word: str, wrd_histogram: dict) -> int:
    count_find_word = 0

    #loop the content of the dictionary to find_word as a dict key
    for key, value in wrd_histogram.items():
        #search the keyword within the histogram dictionary
        if key == find_word:
            #assign value of the found key word to the count_find_word
            count_find_word = value
    
    return count_find_word

def main():
    str_words = 'one fish two fish three fish four fish'
    main_functionality = histogram(str_words)
    histogram_freq = frequency('fish', main_functionality)
    print(histogram_freq)

if __name__ == "__main__":
    main()