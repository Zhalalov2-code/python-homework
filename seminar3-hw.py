#Taskk1
str1 = 'Hello'
str2 = 'World'
res = str1 + ' ' + str2
print(res)

#Task2
str = 'Python is awesome'
res = str * 3
print(res)

#Task3
str = 'Data Science is about working with big data'
res = str.replace("a", '#')
print(res)

#Task4
name = input("Enter your name: ")
surname = input("Enter your surname: ")
print(f"{name} {surname} - отличный студент!")

#Task5
code = input("Пишите регион вашего номера машины: ")
if code == '01':
    print(f'Бишкек {code}')
elif code == '02':
    print(f'Ош {code}')
elif code == '03':
    print(f'Баткен {code}')
elif code == '04':
    print(f'Джалал-Абад {code}')
elif code == '05':
    print(f'Нарын {code}')
elif code == '06':
    print(f'Талас {code}')
elif code == '07':
    print(f'Ыссык-Куль {code}')
elif code == '08':
    print(f'Чуй {code}')
else:
    print('Неизвестный код региона')

#Task6
text = input("Введите текст: ")
res = text.swapcase()
print(res)

#Task7
str = input("Введите что нибудь: ")
if str.isdigit():
    print("Это число")
elif str.isalpha():
    print("Это строка")
else:
    print("Это что-то другое")

#Task8
str = input("Введите строку: ")
if str.startswith('Data Science'):
    print(True)
else:
    print(False)

#Task9
text = 'Python'
text = text[-1] + text[1:-1] + text[0]
print(text)

#Task10
text = 'ABC'
res = text[::-1]
print(res)
