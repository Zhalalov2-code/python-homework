import string
import math 

# Task1
a = "Java"
for i in range(10):
    print(a)

# Task2
user = input("Напишите имя и какоето число через пробел: ")
name, number = user.split()
for i in range(int(number)):
    print(name)

# Task3
for i in range(2, 13):
    print(i)

# Task4
num_listm = []
for i in range(2, 13):
    num_listm.append(i)
print(num_listm)

# Task5
num_list = [1, 3, 2, 5, 4, 3, 6, 7, 8, 7, 9, 8]
for i in num_list:
    if i % 2 == 0:
        print(i)

# Task6
num_list = [1, 3, 2, 5, 4, 3, 6, 7, 8, 7, 9, 8]
for i in range(len(num_list)-1, -1, -1):
    if num_list[i] % 2 != 0:
        remove_item = num_list.remove(num_list[i])
print(num_list)

# Task7
sum = 0
for i in range(4, 22):
    if i % 2 == 1:
        sum += i
print(sum)

# Task8
number = int(input("Введите число: "))
sum = 0
for i in range(1, number + 1):
    sum += i
print(sum)

# Task9
number = int(input("Введите число: "))
sum = 1
for i in range(1, number + 1):
    sum *= i
print(sum)

# Task10
number = int(input("Введите число: "))
res = 0
for i in range(1, number + 1):
    res += i**2 - i
print(res)

# Task11
x = [1, 3, 4, 3, 5, 7, 7, 4, 8, 2, 9, 10, 2, 1, 0]
a = sum(x) / len(x)
for i in x:
    sum += (i - a) ** 2
print(f"Среднее арифметическое: {a}")
print(f"Сумма квадратов отклонений: {sum}")

# Task12
str_ = "Ты виноват лишь в том, что хочется мне кушать..."
words = str_.split()
for word in words:
    cleaned_word = word.strip(string.punctuation)
    print(cleaned_word)

# Task13
str_ = "kjhkj4323kk43kbh543t54"
for i in str_:
    if i.isdigit():
        print(i)

# Task14
word_list = [
    "apple",
    "mountain",
    "astronomy",
    "aerobic",
    "river",
    "ant",
    "airplane",
    "ocean",
    "art",
    "alpine",
    "guitar",
    "atom",
    "dog",
    "alligator",
    "sun",
    "astral",
    "box",
    "amplifier",
]
for i in word_list:
    n = i.capitalize()
    print(n)

# Task15
word_list = [
    "apple",
    "mountain",
    "astronomy",
    "aerobic",
    "river",
    "ant",
    "airplane",
    "ocean",
    "art",
    "alpine",
    "guitar",
    "atom",
    "dog",
    "alligator",
    "sun",
    "astral",
    "box",
    "amplifier",
]
word_with_a = []
for i in range(len(word_list)-1, -1, -1):
    if word_list[i].startswith("a"):
        word_with_a.append(word_list[i])
        word_list.remove(word_list[i])
print("Слова, начинающиеся на 'a':", word_with_a)
print("Оставшиеся слова:", word_list)

# Task16
user_id = [21, 23, 245, 663, 435, 609, 906, 9843]
result = []
for i in user_id:
    new_value = "ID_" + str(i)
    result.append(new_value)
print(result)

# Task17
num_list = [5, 21, 23, 245, 663, 435, 609, 906, 9843]
res = []
for i in num_list:
    num = str(i)
    num = num.zfill(4)
    res.append(num)
print(res)

# Task18
DNA = "AATTAGGATGATCGCTAGGCTCGATAGGCTAGTTCCGGGAGCTGACTGC"
RNA = ""
for i in DNA:
    if i == "T":
        RNA += "U"
    elif i == "T":
        RNA += "A"
    elif i == "A":
        RNA += "U"
    elif i == "G":
        RNA += "C"
    elif i == "C":
        RNA += "G"
    elif i == "C":
        RNA += "G"
print(RNA)

# Task19
DNA = "AATTAGGATGATCGCTAGGCTCGATAGGCTAGTTCCGGGGGGGAGCTGACTGC"
max_len = 1
current_len = 1
for i in range(1, len(DNA)):
    if DNA[i] == DNA[i - 1]:
        current_len += 1
    else:
        current_len = 1
    if current_len > max_len:
        max_len = current_len
print(max_len)

#Task20
str_ = 'ABBCABACBGBCABCGBBCBAG'
unique_str = ''
for i in range(len(str_)):
    if str_.count(str_[i]) == 1:
        unique_str += str_[i]
print(unique_str)

#Task21
str_ = 'ABCABABBCABCGBACBGACFBBBBCCCCBCCCBCCCCGCCCABCCCBAACBCCCCCC'
sort_str = sorted(str_)
current_count = 1
max_count = 1
max_char = ''
for i in range(1, len(sort_str)):
    if sort_str[i] == sort_str[i - 1]:
        current_count += 1
    else:
        current_count = 1
    if current_count > max_count:
        max_count = current_count
        max_char = sort_str[i]
print(max_char, max_count)

#Task22
for x in range(-100, 101):
    y = x**2 + 4*x - 12
    if y == 0:
        print(x)

#Task23
min_value = 9999
for x in range(-100, 101):
    y = x*x - 4*x - 3
    if y < min_value:
        min_value = y
print(min_value)

#Task24
min_value = 9999
min_x = 0
for x in range(-100, 101):
    y = x*x - 4*x - 3
    if y < min_value:
        min_value = y
        min_x = x
print(min_x, min_value)

#Task25
num_list = []
for i in range(10, 31):
    x = i/10
    num_list.append(x)
print(num_list)

#Task26
x = [1, 2, 3, 4, 5, 4]
y = [4, 5, 4, 6, 8, 9]
res = []
for i in range(len(x)):
    summa = x[i] + y[i]
    res.append(summa)
print(res)

#Task27
x = [-3, -2, 1, 3, 5, 6]
y = [0, 3, 4, -2, 4, 1]
z = []
for i in range(len(x)):
    x_i = x[i]
    y_i = y[i]
    z_i = 2*x_i + 0.1*y_i - 5
    z.append(z_i)
print(z)

#Task28
lat = [42.424, 43.345, 41.425, 42.356, 44.653, 41.453]
lon = [63.989, 64.996, 71.654, 72.356, 69.836, 70.909]
cords = []
for i in range(len(lat)):
    coord = (lat[i], lon[i])
    cords.append(coord)
print(cords)

#Task29
min_s = 9999999
best_h = 0
for i in range(1, 101):
   h = i / 10
   a = math.sqrt(32 / h)
   s = a*a + 4*a*h
   if s < min_s:
         min_s = s
         best_h = h
print(best_h, min_s)

#Task30
house_1 = """
Продаю дом с большим участком 8 соток. На участке имеется газ, свет. Есть красная Книга
"""

house_2 = """
Продается дом с ровным участком, Красная книга, газ, вода, телефон все вопросы - звоните отвечу, здравствуйте!
"""

house_3 = """
Продаю ровный дом с остекленным участком, вода есть в наличии водопровод звоните 89 млн сом.
"""

house_4 = """
Здравствуйте! Продается большой дом из 29 комнат. Хорошо проживать большой семьей с видом на горы.
 Присутствует газ и вода. Документы КРАСНАЯ книга, тех паспорт, договор купли продажи звоните
"""
options = ['свет', 'вода', 'красная книга']
res = []
for text in [house_1, house_2, house_3, house_4]:
    text_lower = text.lower()
    svet = 1 if 'свет' in text_lower else 0
    voda = 1 if 'вода' in text_lower else 0
    red_book = 1 if 'красная книга' in text_lower else 0
    res.append((svet, voda, red_book))
print(res)
