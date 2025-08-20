def binary_to_string(binary):
    binary_chunks = binary.split('0b')[1::1]
    result = ''.join(chr(int(b, 2)) for b in binary_chunks)
    return result

print(binary_to_string('0b10000110b11000010b1110100'))



def print_odds(data):
    pass



if __name__ == '__main__':
    binary_to_string('0b10001111110110b11000010b1110100')



class Person:
    name: str
    age: int
    extra_info: dict = {}

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.extra_info = {} #!!!!!!!!!!!!!!!!!!!!!!!!

    def __getitem__(self, item,):
        return self.extra_info[item]

    def __str__(self):
        return f'{self.name}, {self.age}, {self.extra_info}'

vasya = Person('Vasya', 21)
masha = Person('Masha', 22)

vasya.extra_info['description'] = 'student'
masha.extra_info['description'] = 'workworkwork'

print(vasya)
print(masha)


# Задача с собеса
# [1,2,3] -> [1,3,6]
from typing import Iterable

def g(ls: Iterable[int]):
    amount = 0
    for n in ls:
        amount += n
        yield amount

print(g([1,2,3]))
def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()
print(g)

def prefix_sum(arr):
    prefix_sums  = []
    current_sum = 0
    for i in arr:
        current_sum += i
        prefix_sums.append(current_sum)
    return prefix_sums

print(prefix_sum([1,2,3,4]))