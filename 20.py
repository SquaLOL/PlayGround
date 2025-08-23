
def hello(word: str):
    a,b = word.split()
    ar, br = a[::-1], b[::-1]
    m = max(len(a), len(b))
    out = []
    for i in range(m):
        out.append((a[i]) + br[i])
    for y in range(m):
        out.append(b[y] + ar[y])
    return '\n'.join(out)

print(hello("Hello World"))