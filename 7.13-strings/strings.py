# A string is a collection of multiple characters:
string = "abcd"

# Each character is associated with an integer index, starting from 0:
print("string: " + string)
print(" |-- 0: " + string[0])
print(" |-- 1: " + string[1])
print(" |-- 2: " + string[2])
print(" +-- 3: " + string[3])

# These indices could be used to iterate over the characters in a string:
for index in range(0, len(string)):
    print("The character at index " + str(index) + " is " + string[index])

# Alternatively, characters can be accessed relative to the end of the string
#  using negative indices:
print("string: " + string)
print(" |-- -1: " + string[-1])
print(" |-- -2: " + string[-2])
print(" |-- -3: " + string[-3])
print(" +-- -4: " + string[-4])

# Strings can also be "sliced" to extract multiple characters at once:
# NOTE: None of these slices modifies the original string; they all make copies
#       of the string containing the indicated characters.
print("string[1:3]: " + string[1:3])
print("string[1:]: " + string[1:])
print("string[:3]: " + string[:3])
print("string[:]: " + string[:])
print("string[:-1]: " + string[:-1])
