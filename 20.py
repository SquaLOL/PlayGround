def hello(word: str):
    a, b = word.split()
    ar, br = a[::-1], b[::-1]
    m = max(len(a), len(b))
    out = []
    for i in range(m):
        out.append((a[i]) + br[i])
    for y in range(m):
        out.append(b[y] + ar[y])
    return '\n'.join(out)


# print(hello("Hello World"))


def even_odd(arr):
    if not arr:
        return 0
    result = arr[0]
    multiply_next = True
    for x in arr[1:]:
        if multiply_next:
            result *= x
        else:
            result += x
        multiply_next = not multiply_next
    return result


print(even_odd([1, 2, 3]))


def reverse_words(s):
    a, b = s.split()
    return b + ' ' + a
