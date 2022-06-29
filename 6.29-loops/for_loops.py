# Unlike a "while" loop, a "for" loop only runs exactly once for each
#  value in some collection:
for i in range(10):
    print("The current value of i is " + str(i))
    # Note that changing i manually cannot affect the number of iterations;
    #  the "for" loop will overwrite this with the next value in the collection
    #  regardless.
    i = 10

# If two operands are given to "range", the first is the lower bound:
for j in range(5, 10):
    print("The current value of j is " + str(j))

# If three operands are given to "range", the third is the increment:
for k in range(2, 10, 2):
    print("The current value of k is " + str(k))

# Any of these operands may be negative:
for l in range(9, -1, -1):
    print("The current value of l is " + str(l))
