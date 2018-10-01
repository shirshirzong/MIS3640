fin = open("session 9/words.txt")
# print(repr(fin.readline()))

'''Exercise 1_1'''
def read_long_words():
    """
    prints only the words with more than 20 characters
    """
    for line in fin:
        word = line.strip()
        if len(word)>20:
            print(word)


read_long_words()

'''Exercise 1_2'''
def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
    # for letter in word:
    #     # if letter == 'e' or letter == 'E':
    #     if letter.lower() == 'e':
    #         return False
    # return True

    return not 'e' in word.lower()

print(has_no_e('Babson'))
print(has_no_e('College'))


'''Modify program to print only words without 'e' and compute %'''

# def words_without_e():
#     count_no_e_words = 0
#     total_words = 0
#     for line in fin:
#         word = line.strip()
#         total_words += 1
#         if has_no_e(word):
#             print(word)
#             count_no_e_words += 1
#     print('{:.2f}percent of words do not contain "e"'.format(count_no_e_words/total_words))

# words_without_e()


'''Exercise 1_3'''
def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for letter in word:
        return not forbidden in word
    #     if letter in forbidden:
    #         return False
    # return True

print(avoids('Babson', 'ab'))
print(avoids('College', 'ab'))

'''modify program to print words that dont contain a combination of 5 forbidden letters'''
# def words_no_forbidden():
#     forbidden = input ('What letters do you want to forbit?')
#     no_forbidden = 0
#     for line in fin:
#         word = line.strip()
#         if avoids(word, forbidden):
#             no_forbidden += 1
#     print('The number of words that don\'t contain the forbidden letters is: {}'.format(no_forbidden))
# words_no_forbidden()


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
    return True

print(uses_only('Babson', 'aBbsonxyz'))
print(uses_only('college', 'aBbsonxyz'))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in required:
        if letter not in word:
            return False
    return True


print(uses_all('Babson', 'abs'))
print(uses_all('college', 'abs'))


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    previous = ord(word[0])
    for letter in word.lower():
        if ord(letter) < previous:
            return False
        previous = ord(letter)
    return True

print(is_abecedarian('abs'))
print(is_abecedarian('college'))


'''Exercise 2'''
'''rewrite using Recursion'''
def is_abecedarian1(word):
    if len(word) == 1:
        return True
    elif ord(word[1]) < ord(word[0]):
        return False
    else:
        return is_abecedarian1(word[1:])

print(is_abecedarian('abs'))
print(is_abecedarian('college'))

'''rewrite using while loop'''
def is_abecedarian2(word):
    while len(word) > 1:
        if ord(word[1] < ord(word[0])):
            return False
        word = word [1:]
    return True

print(is_abecedarian('abs'))
print(is_abecedarian('college'))