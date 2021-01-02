def print_upper_words(words):
    '''
    to print words uppercase
    '''
    for word in words:
        print(word.upper())


def words_start_with_e(words):
    '''
    to print words that only start with e
    '''
    for word in words:
        if word[0] == 'e' or word[0] == 'E':
            print(word.upper())


def words_must_start_with(words, must_start_with):
    '''
    to pass in a set of letters,
    and it only prints words that start with one of those letters
    '''
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
