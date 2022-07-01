# To define a function that takes no arguments and produces one return value:
def get_leg():
    return int(input("How long is one leg? "))

# To define a function that takes two arguments and produces one return value:
def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

# Functions allow us to write potentially complex code once, use it
#  multiple times, and update it in one place:
side_a = get_leg()
side_b = get_leg()

# Functions allow us to give a readable name to a potentially cryptic
#  chunk of code:
side_c = hypotenuse(side_a, side_b)
print("The hypotenuse has length " + str(side_c))
