def is_max(lst, value):
    """
    Check if a value is the largest in a list.

    :param lst: A list of integers
    :param value: An integer in the list
    :return: Whether or not the integer is greater than or equal to all other
             integers in the list.
    """
    for element in lst:
        if element > value:
            return False
    return True


def max_element(lst):
    """
    Find the largest element in a list.

    :param lst: A list of integers
    :return: The largest integer in the list, or None if the list is empty.
    """
    for element in lst:
        if is_max(lst, element):
            return element
    return None
