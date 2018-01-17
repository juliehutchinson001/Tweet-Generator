def main():
    with open('/usr/share/dict/words') as dictionary_file:
        dictionary_words = dictionary_file.read()

    return dictionary_words