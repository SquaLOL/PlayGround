array = [1,3,2,12,9,423,123,11]

def bubble_sort(arr):
    temp = []
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp =  arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(bubble_sort(array))



def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

print(bool_to_word(False))


def parse_float1(string):
    for i in string:
        if i.isdigit():
            string = float(string)
        break
    if string == str(string):
        return None
    return string


print(parse_float1('123'))


def parse_float2(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None



def boolean_to_string(b):
    return "True" if b == True else "False"

def _all(seq, fun):
    for i in seq:
        if not fun(i):
            return False
    return True


print(_all([1,2,3,4,5], lambda x: x>9))



def socks(colours, pairs):
    return 2 * pairs + (colours - 1)


def skiponacci(n):
    if n <= 0:
        return ""
    result = []
    a, b = 1, 1
    for i in range(n):
        if i % 2 == 0:
            result.append(str(a))
        else:
            result.append("skip")
        a, b = b, a + b
    return ' '.join(result)

    # else:
    #     return (-1)**((n * -1) + 1) * (n * -1)


print(skiponacci(5))