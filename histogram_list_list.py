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

#histogram function counts the freq of words from the sample text
def histogram(str_words):
    # initialize my variables
    subarr_key_value = []

    # receive a string and split it to create an array
    #arr_words = str_words.split()

    # iterate array
    for word_indexed in str_words:
        #condition plus one each repeated word
        ctr_word = str_words.count(word_indexed)
        if [word_indexed, ctr_word] not in subarr_key_value:
            # add new word to list
            subarr_key_value.append([word_indexed, ctr_word])
        
    # call unique_words function to count the total unique words
    print(unique_words(subarr_key_value))

    #return the histogram
    return subarr_key_value

#this function gets a key: [string, ] value: [ , int] pair
def unique_words(subarr_key_value):
    #this returns an integer of the length of types
    return len(subarr_key_value)

def frequency(word_indexed, subarr_key_value):
    #loop the content of array
    for key, value in enumerate(subarr_key_value):
        #search the keyword within the histogram
        if word_indexed in value:
            #assign value of the found key word to the find_word_index
            find_word_index = key
    
    return subarr_key_value[find_word_index][1]


def main():
    #sample string
    str_words = 'one fish two fish three fish four fish'

    #calling function histogram with sample string
    main_functionality = histogram(str_words)

    #calling function unique_words with histogram output as argument
    unique_words(main_functionality)
    
    print(main_functionality)

if __name__ == "__main__":
    main()