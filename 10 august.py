#from preloaded import Like, Dislike, Nothing




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



def to_alternating_case(string):
    temp = ""   # return string.swapcase()
    for i in string:
        if i.isupper():
            temp += i.lower()
        else:
            temp += i.upper()
    return temp


def unusual_five():
    return len("five!")



def least_larger(a, i):
    target = a[i]
    bigger = [x for x in a if x > target]
    if not bigger:
        return -1
    smallest_bigger = min(bigger)
    return a.index(smallest_bigger)




def like_or_dislike(lst):
    transitions = {
        "Nothing":  {"Like": "Like",      "Dislike": "Dislike"},
        "Like":     {"Like": "Nothing",   "Dislike": "Dislike"},
        "Dislike":  {"Like": "Like",      "Dislike": "Nothing"}
    }
    temp = "Nothing"
    for i in lst:
        temp = transitions[temp][i]
    return temp


























