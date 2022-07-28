import string


def sanitize_word(word):
    """
    Remove non-alphabetical characters from a string.
    """
    pass


def count_word(word, counts):
    """
    Count one occurrence of a word.
    """
    pass


def count_words(line):
    """
    Count all of the words in a line.
    """
    pass


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
