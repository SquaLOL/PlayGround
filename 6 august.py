from random import randint

from fontTools.misc.cython import returns

d = {'k1':1,'k2':2,'k3':3}
for key, value in d.items():
    print(key, value)
list(d.keys())
sorted(d.values())
print(sorted(d.values()))

x = 0
while x < 10:
    print('x равен: ',x)
    print(' x всё еще меньше 10, добавляем 1 к x')
    x+=1
    if x==3:
        print('Выходим из цикла (break), потому что x==3')
        break
    else:
        print('продолжаем...')
        continue
else:
    print("Завершено!")


mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
zip(mylist1,mylist2)
list(zip(mylist1,mylist2))

print(randint(1,10))

# Получить все буквы в строке
lst = [x for x in 'word']

# Взять диапазон чисел, возвести их в квадрат, и вернуть в виде списка
lst = [x**2 for x in range(0,11)]
print(lst)

# Сконвертировать градусы Цельсия в градусы Фаренгейта
celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celsius ]


lst4 = [ x**2 for x in [x**2 for x in range(11)]]

st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word.startswith('s'):
        print(word)


# Используйте range(), чтобы распечатать все чётные числа от 0 до 10.
for i in range(0,10):
    if i % 2 == 0:
        print(i)
    else:
        continue
# Используйте генератор списков, чтобы создать список всех чисел от 1 до 50, которые делятся нацело на 3.
div_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print(div_by_3)