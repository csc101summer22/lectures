# A "while" loop should only be used when the desired number of iterations
#  is unknown:
command = input("Enter an initial command: ")
while command != "quit":
    command = input("Enter another command: ")
