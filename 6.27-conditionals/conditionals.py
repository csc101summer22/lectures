# We are allowed to have an "if" all by itself:
if 1 < 2:
    print("1 is less than 2.")

# We can optionally attach an "else" to an "if":
if 1 > 2:
    print("1 is greater than 2.")
else:
    print("1 is not greater than 2.")

# This also works with variables:
x = int(input("Enter a variable x: "))
y = int(input("Enter a variable y: "))

# Additional cases can be added with "elif":
if x > y:
    print("x is greater than y.")
elif x < y:
    print("x is less than y.")
else:
    print("x is equal to y.")

# Note that "if...elif" is not necessarily equivalent to "if...if"; when the
#  conditions are not mutually exclusive, both statements in an "if...if" can
#  execute:
if x > y:
    print("x is strictly greater than y.")
if x >= y:
    print("x is greater than or equal to y.")

# Note that the statements inside a conditional block may be just about any
#  valid Python -- including more conditionals. Conditionals can be "nested":
z = int(input("Enter a variable z: "))

if x > y and x > z:
    print("x is the greatest of x, y, z")
elif y > x and y > z:
    print("y is the greatest of x, y, z")
else:
    print("z is the greatest of x, y, z")

if x > y:
    if x > z:
        print("x is the greatest of x, y, z")
    else:
        # The only way to get to this block is if z >= x > y.
        print("z is the greatest of x, y, z")
else:
    # The only way to get to this block is if y >= x. We still don't know the
    #  answer; but we do now know that the answer is *not* x.
    if y > z:
        print("y is the greatest of x, y, z")
    else:
        print("z is the greatest of x, y, z")
