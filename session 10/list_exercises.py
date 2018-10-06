def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    sum = 0 
    for sublist in t:
        for value in sublist:
            sum += value
    return sum



def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """  
    sum = 0
    newlist = []
    for i in t:
        sum += i
        newlist.append(sum)
    return newlist




def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    return t[1:-1]

# t = [1,2,3,4,5,6,7]
# print(middle(t))
# print(t)


def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    del t[0]
    del t[-1]
    return 

def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    return sorted(t) == t


def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """
    if len(word1) != len(word2):
        return False

    for i in word1:
        if word1.count(i) != word2.count(i):
            return False

    return True

#.count is to count how many times a letter has been appeared in a word


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """
    for i in s:
        if s.count(i) <= 1:
            return False

    return True


def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.
    s: string or list
    returns: bool
    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def main():
    t = [[1, 2], [3], [4, 5, 6]]
    # print(nested_sum(t))

    t = [1, 2, 3]
    # print(cumsum(t))

    t = [1, 2, 3, 4]
    # print(middle(t))

    # chop(t)
    # print(t)

    # print(is_sorted([1, 2, 2]))
    # print(is_sorted(['b', 'a']))

    # print(is_anagram('stop', 'pots'))
    # print(is_anagram('different', 'letters'))
    # print(is_anagram([1, 2, 2], [2, 1, 2]))

    # print(has_duplicates('cba'))
    # print(has_duplicates('abba'))

    # print(has_adjacent_duplicates('cba'))
    # print(has_adjacent_duplicates('abca'))
    # print(has_adjacent_duplicates('abbc'))



if __name__ == '__main__':
    main()