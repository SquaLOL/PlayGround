import cowsay as c
from odd import is_odd
c.cow('Hello')

name = "Niko"
print(is_odd(9))

def hello():
    print("Hello", name)


def add_three_numbers(a, b, z):
    if a != 0 and b != 0 and z != 0:
        return a + b + z
    else:
        return 'Zero'
