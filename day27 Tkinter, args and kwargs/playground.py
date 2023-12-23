total = 0


def add(*args):
    for n in args:
        global total
        total += n
    return total


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

def calculate(n, **kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)
