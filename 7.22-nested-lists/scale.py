def scale_list(lst, scalar):
    """
    Multiply every element of a list by a scalar.

    :param lst: A list of integers
    :param scalar: An integer
    """
    # NOTE: In order to modify the elements within the list, we must know
    #       their indices.
    for index in range(len(lst)):
        lst[index] = lst[index] * scalar

# Since "lst" is a reference to where a list can be found in memory, passing it
#  to a function gives that function access to our copy of the list -- we both
#  have references to the same chunk of memory.
lst = [1, 2, 3, 4]
scale_list(lst, 2)
print(str(lst))

# If we don't want this behavior, one possibility is to make a copy of the list
#  first, and pass that copy to the function:
lst2 = lst.copy()
scale_list(lst2, 3)
print(str(lst))
print(str(lst2))

# Alternatively, we could define a new function that avoids modifying the list
#  it was given:
def scale_new_list(lst, scalar):
    """
    Multiply every element of a list by a scalar.

    :param lst: A list of integers
    :param scalar: An integer
    """
    temp = []

    for index in range(len(lst)):
        temp.append(lst[index] * scalar)

    # NOTE: Since we have created a new list, only we (the function) have a
    #       reference to it; we need to return that reference.
    return temp

lst3 = scale_new_list(lst, 4)
print(str(lst))
print(str(lst2))
print(str(lst3))

def scale_matrix(matrix, scalar):
    """
    Multiply every element of a 2D matrix by a scalar.

    :param matrix: A list of lists of integers
    :param scalar: An integer
    """
    # NOTE: To iterate over one list, we require one loop. To iterate over two
    #       nested lists, we require two nested loops.
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = matrix[row][col] * scalar

matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
scale_matrix(matrix, 2)
print(str(matrix))
