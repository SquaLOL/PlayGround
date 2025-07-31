def invert(lst):
    zero = []
    for i in range(len(lst)):
        zero.append(lst[i])
        zero[i] *= -1
    return zero

arrat = [1,2,3,4,5,6]
print(invert(arrat))

def divisible_by(numbers, divisor):
    numbs = []
    for i in numbers:
        if i % divisor == 0:
            numbs.append(i)
    return numbs

print(divisible_by(arrat,3))

