import math



def sort_array(value):
    sorted = [] # return "".join(sorted(value))
    for i in value:
        sorted.append(i)
    sorted.sort()
    return ''.join(sorted)

print(sort_array("54321"))



import random
class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])
ghost = Ghost()
print(ghost.color)


def is_palindrome(s):
    s = s.lower() # return s.lower() == s.lower()[::-1]
    return s == s[::-1]
print(is_palindrome("Abba"))



def between(a,b):
    cont = [] # return list(range(a,b+1))
    for i in range(a,b + 1):
        cont.append(i)
    return cont


def maps(a):
    return [arr * 2 for arr in a]
    # arr = []
    # for i in a:
    #     arr.append(i * 2)
    # return arr
print(maps([1,2,3]))


def smash(words):
    return ' '.join(words)


print(smash(["hello", "world"]))


def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]
print(two_highest([15,20,20,17]))



def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000




def square_sum(numbers):
    return sum([i**2 for i in numbers])
    # cont = []
    # for i in numbers:
    #     cont.append(i**2)
    # return sum(cont)
print(square_sum([1,2]))




def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)





def wave_sort(a):
    a.sort()
    for i in range(0, len(a) - 1, 2):
            a[i],a[i + 1] = a[i + 1], a[i]
    #return a
print(wave_sort([1, 2, 34, 4, 5, 5, 5, 65, 6, 65, 5454, 4]))
#a1 >= a2 <= a3 >= a4 <= a5




def rotate(xs: list, n: int) -> list:
    if not xs or n == 0:
        return xs
    n = n % len(xs)
    temp = []
    if n > 0:
        temp = xs[-n:] + xs[:-n]
    else:
        temp = xs[-n:] + xs[:-n]
    return temp
  #  n = n % len(arr)
    return arr[-n:] + arr[:-n]


print(rotate([1,2,3,4,5],-1))



def beggars(values, n):
    #return [sum(values[i::n]) for i in range(n)]
    if n == 0:
        return []
    result = [0] * n
    for i, values in enumerate(values):
        result[i % n] += values
    return result


print(beggars([1,2,3,4,5],3))



def reverse(seq):
    up = 0
    down = len(seq) - 1
    while up < down:
        seq[up], seq[down] = seq[down], seq[up]
        up += 1
        down -= 1
    return seq

print(reverse([1,2,3,4]))


def insert_barrels(warehouse, barrels):
    finish = len(barrels)
    index = -1
    best_end = float('inf')

    i = 0
    while i < len(warehouse):
        if warehouse[i] == '':
            start = i
            size = 0
            while i < len(warehouse) and warehouse[i] == '':
                size += 1
                i += 1
            if size >= finish and size < best_end:
                best_end = size
                index = start
        else:
            i += 1
    if best_end == -1:
        return warehouse
    for j in range(finish):
        warehouse[best_end + j] = '0'


    return warehouse







print(insert_barrels(['0','','','0','','','','0'],['0','0']))











