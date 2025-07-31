# data = input("Введите текст: ")
# file = open('data/text.txt', 'w') # 'a' append 'w' write 'r' read
# file.write('Hello\n') # \n перенос строки
# file.write(data + '\n')
# file.close()

file = open('data/text.txt', 'r')
# print(file.read())
for line in file:
    print(line, end="")  # end чтобы убрать пробелы

file.close()


