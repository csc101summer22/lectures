import string


def sanitize_word(word):
    """
    Remove non-alphabetical characters from a string.

    :param word: An arbitrary string
    :return: A lowercased string with punctuation and numbers removed
    """
    result = ""

    for character in word.lower():
        if character.isalpha():
            result = result + character

    return result


def count_word(word, counts):
    """
    Count one occurrence of a word.

    :param word: A sanitized string to count
    :param counts: A dictionary mapping words to frequencies
    """
    if word not in counts and word != "":
        counts[word] = 1
    elif word != "":
        counts[word] = counts[word] + 1


def count_words(line):
    """
    Count all of the words in a line.

    :param line: An arbitrary string of space-separated words
    :return: A dictionary mapping words to frequencies
    """
    counts = {}

    for word in line.split():
        word = sanitize_word(word)
        count_word(word, counts)

    return counts


def main():
    line = input("Enter a line of text: ")
    counts = count_words(line)
    words = [[counts[word], word] for word in counts]
    words.sort(reverse = True)

    print("The most common words are:")
    for i in range(min(len(words), 10)):
        print("%s (%d)" % (words[i][1], words[i][0]))


if __name__ == "__main__":
    main()
