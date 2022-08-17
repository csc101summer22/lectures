def max_element(lst):
    """
    Find the largest element in a list.

    :param lst: A list of integers
    :return: The largest integer in the list, or None if the list is empty.
    """
    temp = None

    for element in lst:
        if temp is None or element > temp:
            temp = element

    return temp
