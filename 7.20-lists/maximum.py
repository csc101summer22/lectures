def max_element(lst):
    """
    Find the largest element in a list.

    :param lst: A list of integers
    :return: The largest integer in the list
    """
    # Initially, assume the first element is the largest:
    temp = lst[0]

    # Go through all the elements:
    for element in lst:
        # Check if we've found a new, larger element:
        if element > temp:
            # If so, that is now the largest seen so far:
            temp = element

    # Once we get to the end of the list, the largest seen so far must also be
    #  the largest seen overall:
    return temp


print(str(max_element([2, 1, 13, 3, 1, 5, 0])))
