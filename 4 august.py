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
    # your code here
    pass