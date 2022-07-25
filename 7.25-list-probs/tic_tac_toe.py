def get_integer(prompt):
    """
    Get an integer between 0 and 2, inclusive, from the user.

    :param prompt: A string to show the user
    :return: The first integer between 0 and 2, inclusive, that the user types
    """
    pass


def check_row(grid):
    """
    Check to see if the game has been won via a row.
    NOTE: We would never want to call this function by itself during the running
          of the program, but decomposing it does allow us to test it by itself.

    :param grid: A 3x3 nested list
    :return: Whether or not the list contains three identical, non-None
             values in a row.
    """
    for row in range(len(grid)):
        if (grid[row][0] != None and grid[row][0] == grid[row][1]
            and grid[row][1] == grid[row][2]):
            # There are three non-Nones in the same row.
            return True

    # NOTE: If we find a winning combination, we can stop early. But only once
    #       we have checked all of the winning possibilities is it safe to
    #       return False.
    return False


def check_column(grid):
    """
    Check to see if the game has been won via a column.

    :param grid: A 3x3 nested list
    :return: Whether or not the list contains three identical, non-None
             values in a column.
    """
    for col in range(len(grid[0])):
        if (grid[0][col] != None and grid[0][col] == grid[1][col]
            and grid[1][col] == grid[2][col]):
            # There are three non-Nones in the same column.
            return True

    return False


def check_diagonal(grid):
    """
    Check to see if the game has been won via a diagonal.

    :param grid: A 3x3 nested list
    :return: Whether or not the list contains three identical, non-None
             values in a diagonal.
    """
    # NOTE: There are only two possible diagonals -- rather than overcomplicating
    #       The code, we could just check each explicity.
    if (grid[0][0] != None and grid[0][0] == grid[1][1]
        and grid[1][1] == grid[2][2]):
        return True

    if (grid[0][2] != None and grid[0][2] == grid[1][1]
        and grid[1][1] == grid[2][0]):
        return True

    return False


def check_grid(grid):
    """
    Check to see if the game has been won.

    :param grid: A 3x3 nested list
    :return: Whether or not the list contains three identical, non-None
             values in a row, column, or diagonal.
    """
    return check_row(grid) or check_column(grid) or check_diagonal(grid)


def main():
    grid = [[None, None, None],
            [None, None, None],
            [None, None, None]]


if __name__ == "__main__":
    main()
