def twice_as_old(dad_years_old, son_years_old):
    age = 0
    age = dad_years_old - (son_years_old * 2)
    if age < 0:
            age = age * -1
    elif son_years_old == 0 or dad_years_old == 0:
            age = dad_years_old
    return age
print(twice_as_old(0  ,0))


def cockroach_speed(s):
    # result = s * 27.77777778
    return int(s * 27.77777778)

print(cockroach_speed(1.08))

def double_char(s):
    word = ''
    for i in s:
        word = word + i * 2
    return word

# print(double_char('Hello'))

def str_count(strng, letter):
    count = 0
    for i in strng:
        if letter == i:
            count += 1
    return count
# print(str_count('Hello', 'l'))

def points(games):
    points = 0
    for i in range(len(games)):
        if games[i][0] > games[i][2]:
            points += 3
        # elif games[i][0] < games[i][2]:
        #     points += 0
        elif games[i][0] == games[i][2]:
            points += 1
    return points

qaz = ['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']
# print(points(qaz))

def fibo (n):
    if n == 0:
        return 0
    elif n == 1 or n == -1:
        return 1
    if n > 0:
        return fibo(n - 1) + fibo(n - 2)
    else:
        return (-1)**((n * -1) + 1) * fibo(n * -1)

print(fibo(5))



def scramble(strng, array):
    result = [''] * len(array)
    for i, y in enumerate(array): # ДВА КЛЮЧА, enumerate - получение доступа как к значениям элементов, так и к их индексам
        result[y] = strng[i]
    return ''.join(result) # ПРЕОБРАЗОВАНИЕ МАССИВА В СТРОКУ
# я ебал, час сидел над ней

print(scramble('abcd', [0,3,1,2]))


ARR = [
 { 'Phase': "Phase 1", 'Step': "Step 1", 'Task': "Task 1", 'Value': "5" },
 { 'Phase': "Phase 1", 'Step': "Step 1", 'Task': "Task 2", 'Value': "10" },
 { 'Phase': "Phase 1", 'Step': "Step 2", 'Task': "Task 1", 'Value': "15" },
 { 'Phase': "Phase 1", 'Step': "Step 2", 'Task': "Task 2", 'Value': "20" },
 { 'Phase': "Phase 2", 'Step': "Step 1", 'Task': "Task 1", 'Value': "25" },
 { 'Phase': "Phase 2", 'Step': "Step 1", 'Task': "Task 2", 'Value': "30" },
 { 'Phase': "Phase 2", 'Step': "Step 2", 'Task': "Task 1", 'Value': "35" },
 { 'Phase': "Phase 2", 'Step': "Step 2", 'Task': "Task 2", 'Value': "40" },
]

day = [1230,199,2301,1230,110001,3021,101010,991,9]

def get_digit_signature(n):
    # Строим частотный вектор из 10 цифр
    freq = [0] * 10
    for ch in str(n):
        freq[int(ch)] += 1
    return tuple(freq)  # hashable key

def digit_permutation(arr):
    groups = []
    keys = []
    for num in arr:
        sig = get_digit_signature(num)

        # Проверяем, есть ли уже такая сигнатура
        found = False
        for i, key in enumerate(keys):
            if key == sig:
                groups[i].append(num)
                found = True
                break
        if not found:
            keys.append(sig)
            groups.append([num])

    return groups


print(digit_permutation(day))


def prod2sum(a, b, c, d):
    pairs = [
        [abs(a * c - b * d), abs(a * d + b * c)],
        [abs(a * c + b * d), abs(a * d - b * c)]
    ]
    # pairs = [sorted(pair) for pair in pairs]
    # unique_pairs = sorted({tuple(pair) for pair in pairs})
    return pairs           #[list(pair) for pair in unique_pairs]


print(prod2sum(1,2,1,3))