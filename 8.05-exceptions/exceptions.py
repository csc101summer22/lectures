def foo():
    # Exceptions can be manually raised with custom messages:
    raise Exception("I have a bad feeling about this...")
    # The following line is unreachable, because the exception above will
    #  stop execution before we get there:
    return 1


def bar():
    # Unlike return values, exceptions cannot be ignored -- if the caller
    #  doesn't handle them, the caller's execution will also be stopped:
    foo()
    # The following line is also unreachable:
    return 2


def main():
    # Exceptions can be handled using "try...except" blocks:
    try:
        bar()
    except ValueError:
        print("Handled a value error...")
    except IndexError:
        print("Handled an index error...")
    except TypeError:
        print("Handled a type error...")
    except:
        print("Handled some other type of error...")


if __name__ == "__main__":
    main()
