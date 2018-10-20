import random
import string
import bisect


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        # INSERT CODE BELOW
        strippables = string.punctuation + string.whitespace
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    return sorted([word for word in hist.items()], key=lambda x: x[1], reverse=True)


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    sorted_words = sorted([word for word in hist.items()], key=lambda x: x[1], reverse=True)
    print(f'The {num} most common words are:')
    for freq, word in sorted_words[0:num]:
        print(word, '\t', freq)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    outliers = {}
    for item in d1:
        if item not in d2:
            outliers[item] = d1[item]
    return outliers


def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    words = []
    for item in hist.keys():
        words.append(item)
    frequencies = []
    sum = 0
    for word, freq in hist.items():
        sum += freq
        frequencies.append(sum)
    random_number = random.randint(0, frequencies[-1])
    return words[bisect.bisect(frequencies, random_number)]





def main():
    hist = process_file('session13/Metabolic_Adaption_to_Climate_and_Distribution_of_the_Raccoon.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    print_most_common(hist, 5)

    words = process_file('session13/words.txt', skip_header=False)

    diff = subtract(hist, words)
    print(diff)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()