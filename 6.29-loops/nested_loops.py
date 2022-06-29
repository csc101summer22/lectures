# The statements inside a loop can be just about anything -- including other
#  loops:
for i in range(2):
    for j in range(3):
        # These statements will execute 6 times:
        print("The current values of i and j are " + str(i) + " and " + str(j))

for j in range(3):
    for i in range(2):
        # These statements will execute 6 times:
        print("The current values of i and j are " + str(i) + " and " + str(j))
