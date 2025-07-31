try:
    x = int(input("Input number: "))
    x += 5
    print(x)
except ValueError:
    print("Введите другое число")

x = 0
while x == 0:
    try:
        x = int(input("Input number: "))
        x += 5
        print(x)
    except ValueError:
        print("Введите другое число") # Эта хрень не завершиться, пока не сработает int


try:
    x = 5 / 0
except ZeroDivisionError:
    print("Delenie na ZERO")
except ValueError:
    print("Вы ввели что то не так")
else:                # else сработает, если выполнился блок Try!
    print("else")

finally:
    print("Finally") # finally сработает в любом случае, и завершит работу














