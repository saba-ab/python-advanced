try:
    x = 1 / 0
except ZeroDivisionError:
    print("you cant divide on zero")
finally:
    print("this prints finaly")
