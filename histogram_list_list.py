'''
Visualizing histogram
original_str = 'one fish two fish three fish four fish'
list_histogram_of_original_str = [[one, 1], [fish, 4], [two, 1], [three, 1], [four, 1]]

>* A histogram() function which takes a source_text argument (can be either a filename or the contents of 
the file as a string, your choice) and return a histogram data structure that stores each unique word 
along with the number of times the word appears in the source text.
>* A unique_words() function that takes a histogram argument and returns the total count of unique words 
in the histogram. For example, when given the histogram for The Adventures of Sherlock Holmes, it returns 
the integer 8475.
>* A frequency() function that takes a word and histogram argument and returns the number of times that 
word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will 
return the integer 20.
'''

def histogram(str_words: str) -> list:
    #TODO: initialize my variables
    subarr_key_value = []

    #TODO: receive a string and split it to create an array
    arr_words = str_words.split()

    #TODO: iterate array
    for word_indexed in arr_words:
        #TODO: condition plus one each repeated word
        if word_indexed in subarr_key_value:
            #TODO: add new word to list
            subarr_key_value.index(word_indexed)[1] += 1
        else:
            #TODO: increment counter for words that already exist
            subarr_key_value.append([word_indexed,0])
            
    #TODO: call unique_words function to count the total unique words
    print(unique_words(subarr_key_value))

    #return dictionary
    return dict_histogram


def unique_words(subarr_key_value: list) -> int:
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
    #sample string
    str_words = 'one fish two fish three fish four fish'

    #calling function histogram with sample string
    main_functionality = histogram(str_words)

    #calling function frequency with histogram output as dict argument
    histogram_freq = frequency('fish', main_functionality)
    
    print(histogram_freq)

if __name__ == "__main__":
    main()