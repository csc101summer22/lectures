# This function is too broad: it attempts to solve two problems at once. In the
#  future, if we only needed to solve one of those problems, it is not possible
#  to call half of this function.
# def main():
#     n = 0
#     while n <= 0:
#         n = int(input("Enter a positive integer: "))
#
#     total = 0
#     for i in range(n + 1):
#         total = total + i ** 2
#
#     print(total)


def get_integer():
    n = 0
    while n <= 0:
        n = int(input("Enter a positive integer: "))
    return n


def sum_squares(n):
    total = 0
    for i in range(n + 1):
        total = total + i ** 2
    return total


# It is always possible to call two functions back-to-back:
def main():
    n = get_integer()
    print(sum_squares(n))


if __name__ == "__main__":
    main()
