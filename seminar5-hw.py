import math
# Task1
task1 = [1, 2, 3, 4, 5]
for i in range(len(task1) - 1, -1, -1):
    if task1[i] % 2 == 0:
        removed_element = task1.pop(i)
        print(f"Removed element: {removed_element}")
print("Final list after removing even numbers:", task1)

# Task2
# Вариант А
n = int(input("Введите цифру: "))
list1 = []
for i in range(n + 1):
    list1.append(str(i))
print(list1)

# Вариант Б
list2 = []
for i in range(len(list1)):
    if i % 2 == 1:
        x = i * 10
        list2.append(str(x))
print(list2)

# Task3
list1 = [1, 22, 3, 45, 22, 4, 89, 87, 87, 4]
task3 = list1[::2]
print("Elements at even indices:", task3)

# Task4
ls = [11, 23, 45, 7, 9]
print(ls[::-1])

# Task5
list1 = []
for i in range(1, 18):
    id = str(i).zfill(4)
    new_value = "ID_" + id
    list1.append(new_value)
print(list1)

# Task6
city = str(input("Введите название города: "))
street = str(input("Введите название улицы: "))
house_number = str(input("Введите номер дома: "))
for i in range(1, 4):
    address = f"г. {city}, ул. {street}, д. {house_number}"
print(address)

# Task7
users = [23, 24, 43, 25, 83]
for i in range(len(users)):
    value = "ID_" + str(users[i])
    users[i] = value
print(users)

# Task8
task8 = "abcdefg12345"
list1 = []
for i in range(len(task8)):
    simbol = list1.append(str(task8[i]))
print(list1)

# Task9
min_s = None
best_t = None
for i in range(1, 25):
    s = 4 * i**2 + (24 - i) ** 2
    if min_s is None or s < min_s:
        min_s = s
        best_t = i
print("Minimum value:", min_s)
print("Best t:", best_t)

# Task10
id_list = ["ID_23", "ID_24", "ID_43", "ID_25", "ID_83"]
for i in range(len(id_list)):
    id_list[i] = int(id_list[i][3:])
print(id_list)

# Task11
num_list = [2, 4, 6, 8, 6, 4, 5]
task11 = []
for i in range(len(num_list)):
    left = num_list[i - 1]
    right = num_list[(i + 1) % len(num_list)]
    task11.append(left + right)
print(task11)

# Task12
task12 = []
for x in range(-100, 101):
    if x * x - 11 * x + 30 == 0:
        task12.append(x)
print(task12)

# Task13
task13 = None
for x in range(-100, 101):
    y = x * x - 8 * x + 3
    if task13 is None or y < task13:
        task13 = y
print(task13)

# Task14
min_x = None
for x in range(-100, 101):
    y = x * x - x - 6
    if min_x is None or y < min_x:
        min_x = y
print(min_x)

# Task15
x_value = None
for x in range(-100, 101):
    y1 = 2 * x - 3
    y2 = -x + 6
    if y1 == y2:
        x_value = x
        break
print(x_value)

# Task16
task16 = [1, 22, 3, 45, 22, 4, 89, 87, 87, 4]
res = []
for i in range(len(task16) - 1, -1, -1):
    if i % 2 == 0:
        removed_element = task16.pop(i)
        res.append(removed_element)
print(res[-1::-1])

# Task17
num_list = [1, 3, "1", 4, "89", 5, "9", 7, "75", 12]
task17 = 0
for i in range(len(num_list)):
    task17 += int(num_list[int(i)])
print(task17)

# Task18
num_list = [1, 22, 3, 45, 22, 4, 89, 87, 87, 4]
start_len = len(num_list) - 1
stop_len = len(num_list) // 2 - 1
step = -1
task18 = []
for i in range(start_len, stop_len, step):
    task18.append(num_list[i])
print(task18)

# Task19
max_sum = 0
best_variant = None

total_girls = 25
total_boys = 20

for girls_A in range(0, 23):
    girls_B = total_girls - girls_A

    if girls_B > 23:
        continue

    boys_A = 22 - girls_A
    boys_B = 23 - girls_B

    if boys_A < 0 or boys_B < 0:
        continue
    if boys_A > total_boys or boys_B > total_boys:
        continue
    if boys_A + boys_B != total_boys:
        continue

    percent_A = girls_A / 22 * 100
    percent_B = girls_B / 23 * 100
    s = percent_A + percent_B

    if s > max_sum:
        max_sum = s
        best_variant = (girls_A, girls_B, boys_A, boys_B)

print("Максимальная сумма процентов:", max_sum)
print("Лучшее распределение:")
print("Класс A: девочек =", best_variant[0], ", мальчиков =", best_variant[2])
print("Класс B: девочек =", best_variant[1], ", мальчиков =", best_variant[3])

# Task20
min_salary = None
best_t = None

total_workers = 24

for t in range(total_workers + 1):
    workers1 = t
    workers2 = total_workers - t

    salary1 = 4 * workers1**2
    salary2 = workers2**2
    total_salary = salary1 + salary2

    if (min_salary is None) or (total_salary < min_salary):
        min_salary = total_salary
        best_t = t

print("Лучшее распределение:")
print("На 1-й объект:", best_t, "чел")
print("На 2-й объект:", total_workers - best_t, "чел")
print("Минимальная общая зарплата:", min_salary, "у.е.")

# Task21
v1 = 40  
v2 = 30  
d1_start = 5 
d2_start = 3 

min_dist = None
best_t = None

t = 0.0
step = 0.001

while t <= 1.0:
    d1 = d1_start - v1 * t
    d2 = d2_start - v2 * t

    dist = math.sqrt(d1**2 + d2**2)

    if (min_dist is None) or (dist < min_dist):
        min_dist = dist
        best_t = t

    t += step

time_minutes = best_t * 60

print("Время, когда расстояние минимально (мин):", time_minutes)
print("Минимальное расстояние (км):", min_dist)
