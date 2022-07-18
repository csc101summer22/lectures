# Check that two DNA strands consist of complementary base pairs.


def get_string(prompt):
    """
    Read a string of A's, C's, G's, and T's from the user.

    :param prompt: A string to show the user
    :return: The next line the user types
    """
    # NOTE: We could check that the strings contain valid bases here, but the
    #       check_bases function already covers that possibility.
    return input(prompt)


def check_bases(base1, base2):
    """
    Check that two bases are complementary.

    :param base1: A character, A, C, G, or T
    :param base2: A character, A, C, G, or T
    :return: Whether or not the characters match
    """
    if base1 == "A":
        return base2 == "T"
    elif base1 == "C":
        return base2 == "G"
    elif base1 == "G":
        return base2 == "C"
    elif base1 == "T":
        return base2 == "A"
    else:
        return False


def check_strands(strand1, strand2):
    """
    Check that two strands are complementary.

    :param strand1: A string of the characters A, C, G, or T
    :param strand2: A string of the characters A, C, G, or T
    :return: Whether or not the strands match pairwise
    """
    if len(strand1) != len(strand2):
        return False

    for index in range(len(strand1)):
        if not check_bases(strand1[index], strand2[index]):
            return False

    return True

def main():
    # Each of the two stands will be a string, consisting of the characters
    #  A, C, G, and T.
    # Information we need from the user:
    #   * The two strands
    strand1 = get_string("Enter the first strand: ")
    strand2 = get_string("Enter the second strand: ")
    # Information we can then compute:
    #   * Whether or not two given bases match
    #   * Whether or not the two strands match pairwise
    if check_strands(strand1, strand2):
        print("The strands match!")
    else:
        print("The strands do not match!")


if __name__ == "__main__":
    main()
