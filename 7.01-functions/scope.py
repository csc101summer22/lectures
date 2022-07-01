def f():
    # NOTE: f does not take x as an argument, but it does have access to the
    #       global x, which is accessible everywhere.
    print("Inside f, x has value " + str(x))

def g():
    # NOTE: This x is local to g. It is separate from the global x, and it is
    #       only accessible inside g.
    x = 2
    print("Inside g, x has value " + str(x))

def h(x):
    # NOTE: Parameters are also local to their functions. Even if the global x
    #       is passed to h, within h, x is still a local.
    x = 4
    print("Inside h, x has value " + str(x))

# This variable is global; it is accessible everywhere:
x = 1
print("Before f, x has value " + str(x))
f()
print("After f and before g, x has value " + str(x))
g()
print("After g and before h, x has value " + str(x))
h(x)
print("After h, x has value " + str(x))
