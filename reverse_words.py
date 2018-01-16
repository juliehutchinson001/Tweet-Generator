def reverse_sentences(sentence):
    sentence_len = len(sentence) - 1
    for word_index in range(0:sentence_len)

def string_reversal(words):
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