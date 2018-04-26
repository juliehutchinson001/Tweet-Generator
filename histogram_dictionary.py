"""
Visualizing histogram.
original_str = 'one fish two fish three fish four fish'
dict_histogram_of_original_str = {one: 1, fish: 4, two: 1, three: 1, four: 1}
"""

class Histogram():
    

    def __init__(self, str_words) -> None:
        """Initialize histogram with words given"""
        self.str_words = str_words
        self.histogram = self.get_histogram()

    def get_histogram(self) -> dict:
        '''Dictionary histogram'''
        # initialize my variables
        dict_histogram = {}

        # receive a string and split it to create an array
        arr_words = self.str_words.split()

        # iterate array
        for word_indexed in arr_words:
            # condition plus one each repeated word
            if word_indexed not in dict_histogram:
                # add new word to dictionary
                dict_histogram[word_indexed] = 1
            else:
                # increment counter for words that already exist
                dict_histogram[word_indexed] += 1

        # return dictionary
        return dict_histogram


    def get_unique_words(self) -> int:
        # #counter tracker for unique words
        # count_values = 0
        # #loop the content of the dictionary
        # for key, value in d_histogram.items():
        #     #count the types in histogram
        #     count_values += 1
        # import pdb; pdb.set_trace()
        return len(self.histogram)

        # return count_values

    def get_frequency(self, find_word: str) -> int:
        # loop the content of the dictionary to find_word as a dict key
        # for key, value in wrd_histogram.items():
        #     #search the keyword within the histogram dictionary
        #     if key == find_word:
        #         # When find_word found return the value
        #         return value

        return self.histogram[find_word] if find_word in self.histogram else 0


def main():
    #sample string
    # str_words = 'one fish two fish three fish four fish'

    #accessing the list of words as string
    helper_dictionary_words = get_long_words()
    # helper_dictionary_words = get_words()
    # helper_dictionary_words = get_short_words()

    #calling function histogram with sample string
    histogram = Histogram(get_long_words())
    # histogram = Histogram(helper_dictionary_words)
    # histogram = Histogram(get_short_words())

    #calling function frequency with histogram output as dict argument
    histogram_freq = histogram.get_frequency('Alice')

    print('Alice tokens: ', histogram_freq)
    print('Total amount of types: ', histogram.get_unique_words())
    print('Alice should be: ', histogram.get_frequency('Alice') / sum(histogram.histogram.values()))


if __name__ == "__main__":
    main()
