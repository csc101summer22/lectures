# To repeat statements until a condition is no longer true:

i = 0
while i < 10:
    print("The current value of i is " + str(i))
    i = i + 1

print("This only executes once i >= 10.")

# It is possible for a loop to only run once:

j = 0
while j < 10:
    print("The current value of j is " + str(j))
    j = 10

# It is also possible that a loop never runs at all:

k = 0
while k > 10:
    print("The current value of k is " + str(k))
    k = k + 1
