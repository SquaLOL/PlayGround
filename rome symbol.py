def solution(roman : str) -> int:
    roman_words = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    numbers = 0
    old_numbers = 0
    for i in reversed(roman):
        value = roman_words[i]
        if value < old_numbers:
            numbers -= value
        else:
            numbers += value
            old_numbers = value

    return numbers

print(solution('MMMCMXCIX'))

# class Greek:
#     def __init__(self, I, V, X, L, C, D, M):
#         self.I = 1
#         self.V = 5
#         self.X = 10
    #         self.L = 50
    #         self.C = 100
    #         self.D = 500
    #         self.M = 1000
    # return
x = y = z = 0
a = 2
b = 5
tp1,tp2 = a, b

print(tp1)