def monkey_count(n):
    monkey = []
    for i in range(n):
        monkey.append(i + 1)
    return monkey


print(monkey_count(3))


def calculator(x, y, op):
    result = "unknown value"
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(op, str):
        result = "unknown value"
    elif op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        result = x / y

    return result


print(calculator(1, 5, '+'))
