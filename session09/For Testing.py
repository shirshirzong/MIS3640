def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    before = word[0]
    for letter in word:
        if letter < before:
            return False
        before = letter
    return True


# def find_abecedarian_words():
#     fin = open('session 9/words.txt')
#     counter = 0
#     current_longest_word = ''
#     for line in fin:
#         word = line.strip()
#         if is_abecedarian(word):
#             # print(word)
#             counter += 1
#             if len(word) > len(current_longest_word):
#                 current_longest_word = word

#     return counter, current_longest_word


# print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_using_recursion(word[1:])

print(is_abecedarian_using_recursion('b'))