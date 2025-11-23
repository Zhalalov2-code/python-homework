# Task1
# Создайте список из 10 строк 'I`m_str'
list_ = ["I'm_str" for i in range(10)]
print(list_)

# Создайте список из 10 нулей
zeros = [0 for i in range(10)]
print(zeros)

# Task2
# Создайте список из чисел от 1 до 15 в формате 'int'.
nums = [i for i in range(1, 16)]
print(nums)

# Task3
# Дана строка. С помощью list comprehension сделайте список из всех элементов данной строки.
str_ = "abc123"
task3 = [i for i in str_]
print(task3)

# Task4
# Создайте список чисел на множестве [10;100] шагом 10, где каждое число будет в формате строки.
task4 = [str(i) for i in range(10, 101, 10)]
print(task4)

# Task5
# Создайте список чисел на множестве [1; 3] шагом 0.1, где каждое число будет в формате строки строго как в образце!
task5 = [f"{i:.1f}" for i in [j / 10 for j in range(10, 31)]]
print(task5)

# Task6
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
task_n = [f"task_{i}" for i in n]
print(task_n)

# Task7
# Дан список с именами файлов с выполненными домашними работами студентов. Название файла генерируется из названии домашней работой студента и его gmail. В конце названия присутствует расширение '.ipynb'.Сформируйте список, состоящий только из gmail студентов.
students = [
    "Answer_DZ_3-yudkevyc.v@gmail.com.ipynb",
    "Answer_DZ_3-eshmukhamedoa@gmail.com.ipynb",
    "Answer_DZ_3-amiimere@gmail.com.ipynb",
    "Answer_DZ_3-abin.saubanova@gmail.com.ipynb",
    "Answer_DZ_3-abyv56@gmail.com.ipynb",
    "Answer_DZ_3-selgizbaeva@gmail.com.ipynb",
    "Answer_DZ_3-irzaimovazhibek@gmail.com.ipynb",
    "Answer_DZ_3-jarida@gmail.com.ipynb",
    "Answer_DZ_3-naa.zhaparov@gmail.com.ipynb",
    "Answer_DZ_3-edrymanaliev4@gmail.com.ipynb",
    "Answer_DZ_3-ikn.akmatova@gmail.com.ipynb",
    "Answer_DZ_3-ekaeenalieva@gmail.com.ipynb",
    "Answer_DZ_3-ulanovaaziza313@mail.ru.ipynb",
    "Answer_DZ_3-umk.kg@gmail.com.ipynb",
    "Answer_DZ_3-lar.bojokoev@gmail.com.ipynb",
    "Answer_DZ_3-adshov.s@gmail.com.ipynb",
    "Answer_DZ_3-ndiakaidueva@gmail.com.py",
    "Answer_DZ_3-ultaovbekma@gmail.com.ipynb",
    "Answer_DZ_3-lexosankov@gmail.com.ipynb",
    "Answer_DZ_3-izarsesbaev@gmail.com.ipynb",
    "Answer_DZ_3-isuuu.lanbetova@gmail.com.ipynb",
]
task7 = [i.split("-")[1].replace(".ipynb", "").replace(".py", "") for i in students]
print(task7)

# Task8
# Используя условие if в генераторе списка сформируйте список только четных чисел на множестве [0;20]
nums = [i for i in range(1, 21) if i % 2 == 0]
print(nums)

# Taks9
students = [
    "Answer_DZ_1-isuluu (1).kalmanbetova@gmail.com.ipynb",
    "Answer_DZ_1-isuluu.kalmanbetova@gmail.com.ipynb",
    "Answer_DZ_1-adyshov.s@gmail.com.ipynb",
    "Answer_DZ_3-yudkevych.v@gmail.com.ipynb",
    "Answer_DZ_1-selegizbaeva@gmail.com.ipynb",
    "Answer_DZ_2-adyshov.s@gmail.com.ipynb",
    "Answer_DZ_1-ekajeenalieva@gmail.com.ipynb",
    "Answer_DZ_1-abyev56@gmail.com.ipynb",
    "Answer_DZ_2-selegizbaeva@gmail.com.ipynb",
    "Answer_DZ_2-irzakimovazhibek@gmail.com.ipynb",
    "Answer_DZ_2-ldar.bojokoev@gmail.com.ipynb",
    "Answer_DZ_4-yudkevych (1).v@gmail.com.ipynb",
    "Answer_DZ_2-imonlobgromov@gmail.com.ipynb",
    "Answer_DZ_1-izaersesbaev@gmail.com.ipynb",
    "Answer_DZ_2-ekturamatov@gmail.com.ipynb",
    "Answer_DZ_2-amilimere@gmail (1).com.ipynb",
    "Answer_DZ_2-aimbekovakamila@gmail.com.ipynb",
    "Answer_DZ_2-nara.zhaparov@gmail.com.ipynb",
]
task9 = [
    i.split("-")[1].replace(".ipynb", "").replace(".py", "").replace(" (1)", "")
    for i in students
    if "DZ_2" in i
]
print(task9)

# Task10
# Дан список с результатами проверки домашней работы студента с строками 'yes'/'no'. На основе данного списка составте бинарный:
check_list = ["yes", "no", "no", "no", "yes", "no", "yes", "yes", "yes"]
binary_list = [1 if i == "yes" else 0 for i in check_list]
print(binary_list)

# Task11
#Дана строка. Вытащите из нее только числа и сложите их в отдельный список.
str_ = """
Предприятие N, которое было запущено в 1976 году к 25 съезду КПСС, в этом году наростило выпуск готовой продукции
на 20%. Из выпущенных холодильников, в этому году их количество на 100 едениц превысило выпуск прошлого года. Мы идем поставленным Партией
курсом на увеличение мощностей по выпуску товаров народного потребления: в текущем году товары народного потребления составили 65% от всей производимой номенклатуры.
Мы планируем наростить процент выпускаемой продукции на следующие 5 лет на 40%. Поставленные планы будут выполнены!
"""
only_nums = [int(i) for i in str_.split() if i.isdigit()]
print(only_nums)

# Task12
#Дан список возможных значений цвета. Сформируйте список из 10 элементов, отбирая рандомно один из представленных цветов. Используйте функцию randint().
from random import randint
color_list = ['red', 'blue', 'green']
res_list = [color_list[randint(0, 2)] for i in range(10)]
print(res_list)

# Task13
#Даны два списка с катетами для серии прямоугольных траугольников.Для каждого треугольника расчитайте:Гипотенузу,Тангенс Наименьшего угла
#Синус наименьшего угла, Наименьший острый угол Площадь каждого.
#Площадь описанной окружности для каждого.
#(Радиус описанной окружности вокруг прямоугольного треугольника равен половине гипотенузы)
from math import *
katet_1 = [3, 5, 4, 6, 7, 9, 3, 4, 1, 5]
katet_2 = [6, 4, 5, 2, 7, 9, 1, 5, 4, 3]
hypotenuse = [sqrt(katet_1[i]**2 + katet_2[i]**2) for i in range(len(katet_1))]
tangent = [min(katet_1[i], katet_2[i]) / max(katet_1[i], katet_2[i]) for i in range(len(katet_1))]
sine = [min(katet_1[i], katet_2[i]) / hypotenuse[i] for i in range(len(katet_1))]
smallest_angle = [degrees(asin(sine[i])) for i in range(len(katet_1))]
area = [(katet_1[i] * katet_2[i]) / 2 for i in range(len(katet_1))]
circumscribed_circle_area = [pi * (hypotenuse[i] / 2)**2 for i in range(len(katet_1))]
print("Гипотенуза:", hypotenuse)
print("Тангенс наименьшего угла:", tangent)
print("Синус наименьшего угла:", sine)
print("Наименьший острый угол (градусы):", smallest_angle)
print("Площадь каждого треугольника:", area)
print("Площадь описанной окружности для каждого треугольника:", circumscribed_circle_area)

# Task14
#Даны 3 списка с результатами по контрольным работам школьников. Балл за четверть выставляется как среднее этих оценок. При этом округление происходит по порогу 0.7, что означает, что при среднем балле 3.5, выставляется оценка 3, а при среднем балле 3.7 - оценка 4.
cw_1 = [2, 4, 4, 5, 3, 3, 5, 4, 2, 3]
cw_2 = [5, 4, 4, 3, 4, 3, 4, 5, 3, 5]
cw_3 = [3, 4, 4, 4, 5, 5, 4, 3, 3, 2]
final_grades = [i if (cw_1[idx] + cw_2[idx] + cw_3[idx]) / 3 < int((cw_1[idx] + cw_2[idx] + cw_3[idx]) / 3) + 0.7 else i + 1 for idx, i in enumerate([int((cw_1[i] + cw_2[i] + cw_3[i]) / 3) for i in range(len(cw_1))])]
print(final_grades)

#Task15
#Даны ID пользователей сайте. Переведите их в формат 'ID_00000':
id_list = [23, 245, 3, 3245, 23456, 2, 12, 134, 43, 2311, 23, 95]
formatted_ids = [f"ID_{i:05d}" for i in id_list]
print(formatted_ids)

# Task16
#Даны два списка. Cоздайте список, содержащий элементы, общие для этих двух списков.
list_1 = ['a', 'b', 'c', 2, 4, 6, 8, 'f']
list_2 = [4, 6, 10, 13, 'b', 'c', 'g', 'r']
common_elements = [i for i in list_1 if i in list_2]
print(common_elements)
 
#Task17
#Зигзаг-перестановка: Дан список чисел. Cоздайте новый список, в котором четные индексы имеют возрастающий порядок, а нечетные - убывающий.
list_ = [1, 3, 5, 4, 2, 6, 'a', 'b', 'c', 'd', 'q']

even_nums = [list_[i] for i in range(len(list_)) if i % 2 == 0 and isinstance(list_[i], int)]
even_strs = [list_[i] for i in range(len(list_)) if i % 2 == 0 and isinstance(list_[i], str)]
odd_nums = [list_[i] for i in range(len(list_)) if i % 2 != 0 and isinstance(list_[i], int)]
odd_strs = [list_[i] for i in range(len(list_)) if i % 2 != 0 and isinstance(list_[i], str)]

even_sorted = sorted(even_nums) + sorted(even_strs)
odd_sorted = sorted(odd_nums, reverse=True) + sorted(odd_strs, reverse=True)

zigzag_list = []
even_count = 0
odd_count = 0
for i in range(len(list_)):
    if i % 2 == 0:
        zigzag_list.append(even_sorted[even_count])
        even_count += 1
    else:
        zigzag_list.append(odd_sorted[odd_count])
        odd_count += 1

print("Исходный список:", list_)
print("Зигзаг-перестановка:", zigzag_list)

# Task18
#Дан массив чисел. Выполните нормализацию списка, то есть приведите все числа в диапазон значений [0; 1]. Для этого можно воспользоваться формулой:
list_ = [129, 200, -300, -28, 1, 123, -132, -53, 43, 200, 79, 193, -79]
min_val = min(list_)
max_val = max(list_)
normalized_list = [(i - min_val) / (max_val - min_val) for i in list_]
print("Исходный список:", list_)
print("Нормализованный список:", normalized_list)

# Task19
#Дан массив чисел. Выполните его стандартизацию. Для этого воспользуйтесь формулами: Где - среднее арифметическое. - стандартное отклонение, которое можно вычислить по формуле:
list_ = [150, 149, 178, 170, 200, 198, 189, 161, 171, 164, 195, 186]
mean = sum(list_) / len(list_)
std_dev = (sum((i - mean) ** 2 for i in list_) / len(list_)) ** 0.5
standardized_list = [(i - mean) / std_dev for i in list_]
print("Исходный список:", list_)
print("Стандартизованный список:", standardized_list)
     