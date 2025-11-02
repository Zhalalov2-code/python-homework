#Task1
a = 3
if(a > 0):
    print(True)
else:
    print(False)

#Task2
mark = int(input("Введите число: "))
if(mark >= 90):
    print('Отлично, Ваша оценка 5!')
elif(mark >= 80 and mark < 90):
    print('Хорошо, Ваша оценка 4!')
elif(mark >= 70 and mark < 80):
    print('Удовлетворительно, Ваша оценка 3!')
elif(mark < 70):
    print('Попробуйте еще раз, Ваша оценка 2!') 

#Task3
x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

if x <= y and x <= z:
    print(x)
elif y <= x and y <= z:
    print(y)
else:
    print(z)

#Task4
a = int(input("Введите число: "))
b = int(input("Введите число: "))
res = a / b
if (res % 2 == 0 ):
    print(res)
else:
    print(res)

#Task5
a = 4
b = 9
c = 6

if a + b > c and a + c > b and b + c > a:
    print("yes")
else:
    print("no")

#Task6
a = 58
b = 5
c = 63
res = a + b
if (res == c):
    print('Yes')
else:
    print('No')

#Task7
a = int(input("Введите число: "))
if (a >= 2 and a < 10):
    print(True)
else:
    print(False)

#Task8
x = int(input("Введите цифру: "))
if (x < 4 ) or (x >= 5):
    print(True)
else:
    print(False)

#Task9
x = int(input("Введите цифру: "))
if (x % 2 == 0):
    print(True)
else:
    print(False)

#Task10
x = int(input("Введите цифру: "))
if (x > -10 and x < 5) or (x > 5 and x <= 7) or (x > 8):
    print(True)
else:
    print(False)

#Task11
x = float(input("Введите число x: "))

if x == -5 or x == 7:
    print("Деление на ноль невозможно")
else:
    left = (x**2 - 3*x) / (x + 5)
    right = (x - 3) / (7 - x)
    print(left >= right)

#Task12
x = float(input("Введите число: "))
cond1 = (x**2 - 3*x) <= 0
cond2 = (x**2 - 6*x + 8) > 0

if cond1 and cond2:
    print("True")
else:
    print("False")

#Task13
x = float(input("Введите число: "))

if (x > 8) or (x <= 2):
    print("True")
else:
    print("False")