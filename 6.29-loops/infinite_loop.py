# If the condition of a loop is never false, it will run forever:
i = 0
while i < 10:
    print("The current value of i is " + str(i))
    i + 1

print("This only executes once i >= 10.")
