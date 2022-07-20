# A list is essentially a string whose elements may have any type:
print(str(['a', 'b', 'c']))
print(str([1, 2, 3]))

# The basic concatentation and indexing operations still work on lists:
lst = [2, 3]
print(str([1] + lst))
print(str(lst[0]))
print(str(lst[1:]))
print(str(lst == [3, 2]))
print(str("2" in lst))

# Unlike strings, many list operations modify an existing list, rather than
#  creating a new list:
print(str(lst.reverse()))
print(str(lst))

# Creating new lists takes longer than modifying existing lists -- if the
#  programmer knows they actually need a new list, then they should explicitly
#  make a copy first:
lst2 = lst.copy()
lst2.append(4)
lst2.sort()
print(str(lst))
print(str(lst2))

# A list comprehension tells the interpreter *how* to create the elements,
#  rather than *what* the elements are:
print(str([x * 2 for x in range(10)]))

# A list comprehension may optionally include a condition:
print(str([x for x in range(10) if x % 2 == 1]))
