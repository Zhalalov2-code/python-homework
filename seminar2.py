import math

# Task1
a = int(input("Введите цифру: "))
if a > 5:
    print(True)
else:
    print(False)

# Task2
a = int(input("Введите число: "))
if a % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

# Task3
a = int(input("Введите число: "))
b = int(input("Введите число: "))
if a == 2 * b:
    print("Первое число в два раза больше второго")
else:
    print("Первое число не в два раза больше второго")

# Task4
a = int(input("Введите число: "))
if (a != 0) and (a % 3 == 0):
    print("Число делится на 3")
else:
    print("Число не делится на 3")

# Task5
a = int(input("Введите число: "))
if a % 2 == 0:
    print(f"Число четное: {a}")
else:
    a += 1
    print(f"Число нечетное, добавляем 1: {a}")

# Task6
a = int(input("Введите число: "))
if (a > 0) and (a < 10):
    print("Yes")
else:
    print("No")

# Task7
a = int(input("Введите число: "))
if (a >= 5) and (a < 15) and (a != 10):
    print("Yes")
else:
    print("No")

# Task8
a = int(input("Введите число: "))
if (a <= 5) or (a > 10):
    print("Yes")
else:
    print("No")

# Task9
a = int(input("Введите число: "))
if (a > 2 and a <= 6) or (a > 10):
    print("Yes")
else:
    print("No")

# Task10
a = int(input("Введите число: "))
if (a < 4 or a > 10) or (2 <= a <= 6):
    print("Yes")
else:
    print("No")

# Task11
a = float(input("Введите число: "))
if (a <= 3) or (a > 5):
    print("Yes")
else:
    print("No")

# Task12
a = int(input("Введите число: "))
res1 = (a < 3) and (a >= 6)
res2 = a >= 4
res3 = (a > 2 and a < 6) or (a > 5)
res4 = (a > 0 and a < 4) or (a > 5 and a < 10)
print(res1)
print(res2)
print(res3)
print(res4)

# Task13
a = int(input("Введите угол входа: "))
if (a < 40) or (a > 45):
    print("Параметры оптимальны")
else:
    print("Корабль разрушится в атмосфере")

# Task14
x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))
y_line = 0.5 * x + 4
if y > y_line:
    print("Точка выше прямой")
elif y < y_line:
    print("Точка ниже прямой")
else:
    print("Точка лежит на прямой")

# Task16
a = float(input("Введите число: "))
res = math.sqrt(a)
if res < a / 3:
    print("Yes")
else:
    print("No")

# Task17
a = int(input("Введите число: "))
b = int(input("Введите число: "))
summa = a + b
raznost = a - b

if summa > 0 and raznost > 0:
    print("++")
elif summa > 0 and raznost < 0:
    print("+-")
elif summa < 0 and raznost > 0:
    print("-+")
else:
    print("--")

# Task18
a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")

# Task19
a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
res = max(a, b, c)
storony = [a, b, c]
storony.remove(res)
if abs(res**2 - (storony[0]**2 + storony[1]**2)) < 0.001:
    print("Треугольник прямоугольный")
else:
    print("Треугольник не прямоугольный")