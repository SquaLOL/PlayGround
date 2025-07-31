

from  mymodule import add_three_numbers as add
# print(add(1,2,4))
# Написать функцию, которая переводит из десятичной системы исчисления в N ( 2 - 16 )

# Написать функцию, которая переводит из N исчисления в десятичную системы ( 2 - 16 )

def filipp(number, n):
    if not (2 <= n <= 16):
        raise ValueError("Value must be from 2 to 16")
    digits = "0123456789ABCDEF"
    result = ""
    if number == 0:
        return '0'
    while number > 0:
        remainder = number % n
        result = digits[remainder] + result
        number = number // n
    return result




a = [1,2,3,'1']

def sum_mix(arr) -> int:
    cont = 0
    for i in range(len(arr)):
        cont += int(arr[i])
    return cont




def switch_it_up(number):
    word = ['Zero','One','Two','Three', 'Four','Five','Six','Seven','Eight','Nine']
    return word[number]




# print(switch_it_up(0))


