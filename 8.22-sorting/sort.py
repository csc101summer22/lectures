def sort(lst):
    """
    Sort a list of integers in ascending numerical order.

    :param lst: A unsorted list of integers
    :return: A new list containing the same elements, in sorted order
    """
    result = []

    while len(lst) > 0:
        temp = min(lst)
        result.append(temp)
        lst.remove(temp)

    return result
