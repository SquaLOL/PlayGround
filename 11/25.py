def sum_array(a):
    return sum(a)


def make_upper_case(s):
    return s.upper()


def opposite(number):
    return (number * -1)


def get_age(age: str) -> int:
    return int(age[0])

    # def get_age(age):
    return int(age[0])


def sorter(textbooks):
    upper_textbooks = [w.upper() for w in textbooks]
    return sorted(upper_textbooks)


def duty_free(price, discount, holiday_cost):
    savings = price * discount / 100
    return holiday_cost // savings


def is_palindrome(s):
    return s.lower() == s[::-1]


print(is_palindrome('abbbac'))
