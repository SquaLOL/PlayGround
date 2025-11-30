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
    return s.lower() == s.lower()[::-1]


print(is_palindrome('abbac'))

arr = [1, 2]


def swap_values(args):
    args[0], args[1] = args[1], args[0]


def high_and_low(numbers):
    numbers = numbers.split()
    numbers = [i for i in numbers]
    return str(max(numbers)) + ' ' + str(min(numbers))


def sing():
    song = ["99 bottles of beer on the wall, 99 bottles of beer.",
            "Take one down and pass it around, 98 bottles of beer on the wall.",
            "98 bottles of beer on the wall, 98 bottles of beer.",

            "...and so on...",

            "3 bottles of beer on the wall, 3 bottles of beer.",
            "Take one down and pass it around, 2 bottles of beer on the wall.",
            "2 bottles of beer on the wall, 2 bottles of beer.",
            "Take one down and pass it around, 1 bottle of beer on the wall.",
            "1 bottle of beer on the wall, 1 bottle of beer.",
            "Take one down and pass it around, no more bottles of beer on the wall.",
            "No more bottles of beer on the wall, no more bottles of beer.",
            "Go to the store and buy some more, 99 bottles of beer on the wall."]

    return song


def bubblesort_once(arr):
    new_array = arr[:]
    for i in range(len(new_array) - 1):
        if new_array[i] > new_array[i + 1]:
            new_array[i], new_array[i + 1] = new_array[i + 1], new_array[i]
    return new_array


print(bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]))
