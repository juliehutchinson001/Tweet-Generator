def reverse_sentences(sentence: str) -> str:
    
    sentence_arr = sentence.split()
    sentence_len = len(sentence_arr) - 1

    reversed_sentence = ""
    for word_index in range(sentence_len, -1, -1):
        reversed_sentence += ' ' + sentence_arr[word_index] + ' '

    return reversed_sentence.strip()


def string_reversal(words: str) -> str:
    reversed_chars = ""
    reversed_chars += words[::-1]
    return reversed_chars

def main():
    a_new_sentence = "Hello there! my name is 'Julie', what's your name?"
    new_string = "Esternocleidomastoideo"

    print(reverse_sentences(a_new_sentence))

    print(string_reversal(new_string))

if __name__ == "__main__":
    main()