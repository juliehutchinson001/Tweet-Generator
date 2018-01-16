def reverse_sentences(sentence: str) -> str:
    # One liner
    # test = ' '.join(sentence.split()[::-1])

    # splitting the new list of strings
    sentence_arr = sentence.split()

    #reading the length of the array for iteration purposes
    sentence_len = len(sentence_arr) - 1

    reversed_sentence = ""
    
    #iteration of indexes of array
    for word_index in range(sentence_len, -1, -1):

        #concatenation of new reversed string
        reversed_sentence += sentence_arr[word_index] + ' '

    #returning the new reversed statement
    return reversed_sentence.strip()


def string_reversal(words: str) -> str:
    #inspecting the string from left to right
    reversed_chars = words[::-1]
    #returning the new reversed characters
    return reversed_chars

def main():
    a_new_sentence = "Hello there! my name is 'Julie', what's your name?"
    new_string = "Esternocleidomastoideo"

    print(reverse_sentences(a_new_sentence))

    print(string_reversal(new_string))

if __name__ == "__main__":
    main()