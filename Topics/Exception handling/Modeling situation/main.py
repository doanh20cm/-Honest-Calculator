def exception_test():

    raise ZeroDivisionError
    raise ArithmeticError


try:
    exception_test()
except AssertionError:
    print("AssertionError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")