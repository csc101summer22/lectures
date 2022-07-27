# A dictionary is essentially a list whose indices may have any type:
dct = {"a": "alpha", "b": "beta", "c": "gamma"}

# Just like lists, a dictionary is passed as a reference to a chunk of memory;
#  modifying a dictionary inside a function modifies the original copy:
def uppercase_values(dct):
    for key in dct:
        dct[key] = dct[key].upper()

# If a function needs to avoid modifying the original copy, it could create and
#  later return a new dictionary instead:
def invert(dct):
    result = {}

    for key in dct:
        result[dct[key]] = key

    return result

uppercase_values(dct)
print(dct)
inverted = invert(dct)
print(dct)
print(inverted)
