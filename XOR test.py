from xmlrpc.client import Boolean


def sum_mul(n, m):
    if n <= 0 or m <= 0:
            return 'INVALID'
    return sum(range(n, m, n))


print(sum_mul(2,21))


def logical_calc(booleans, operator):
    if operator == "AND":
        return all(booleans)
    elif operator == "OR":
        return any(booleans)
    elif operator == "XOR":
        element = booleans[0]
        for i in range(1, len(booleans)):
            element = element != booleans[i]
        return element

        # if lambda booleans: i ^ operator:
            #     return True
            # else:
            #     return False



