# NOTE: This is the "entry point", the beginning of the file that will be
#       run from the command line.

# To import the definitions found in "functions.py":
import functions

# To import the definitions found in the standard math library:
import math

# NOTE: By convention, code for the entry point is encapsulated in a function
#       named "main".
def main():
    # To use the definitions found in "functions.py":
    side_a = functions.get_leg()
    side_b = functions.get_leg()

    # To use the definitions found in the standard math library:
    side_c = math.hypot(side_a, side_b)
    print("The hypotenuse has length " + str(side_c))

# NOTE: We still have to call the main function; it doesn't get called
#       automatically for us. However, we only want to call the main function
#       if this was the module run from the command line.
if __name__ == "__main__":
    main()
