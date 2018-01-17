'''
Visualizing histograms
original_str = 'one fish two fish three fish four fish'
dict_histogram_of_original_str = {one: 1, fish: 4, two: 1, three: 1, four: 1}

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

def histogram(str_words):
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

    #return dictionary
    return dict_histogram


def main():
    str_words = 'one fish two fish three fish four fish'
    print(histogram(str_words))

if __name__ == "__main__":
    main()