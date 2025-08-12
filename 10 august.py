def solution(stones):
    count = 0
    for i in range(len(stones) - 1):
        if stones[i] == stones[i + 1]:
            count += 1
    return count

print(solution("RRRRGGGGBBBB"))
print(solution("RGBRGB"))
print(solution("RRGGBB"))



def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return sum(numbers[:2])



def reject(seq, predicate):
    result = []
    for x in seq:
        if not predicate(x):
            result.append(x)
    return result


def sp_eng(sentence):
    if "english" in sentence.lower():
        return True
    else:
        return False


print(sp_eng("engliish"))





















