def get_integer():
    n = 0
    while n <= 0:
        n = int(input("Enter a positive integer: "))
    return n


# These functions are too specific: because they include the detail of their
#  respective powers, they can only solve their respective problems, despite
#  how similar the rest of the code is:
# def sum_squares(n):
#     total = 0
#     for i in range(n + 1):
#         total = total + i ** 2
#     return total
#
#
# def sum_cubes(n):
#     total = 0
#     for i in range(n + 1):
#         total = total + i ** 3
#     return total


# To abstract away that detail as a second parameter:
def sum_powers(n, power):
    total = 0
    for i in range(n + 1):
        total = total + i ** power
    return total


def main():
    n = get_integer()

    # To provide that detail on the fly as a second argument:
    print(sum_powers(n, 2))
    print(sum_powers(n, 3))


if __name__ == "__main__":
    main()
