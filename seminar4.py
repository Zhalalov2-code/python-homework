#Task1 
list1 = []
list2 = list()

Type_of_list1 = type(list1)
Type_of_list2 = type(list2)

print(Type_of_list1)
print(Type_of_list2)

#Task2
list3 = [1, 2, 3, 4, 5]
print(list3)

#Task3
list4 = list(range(1, 21))
print(list4)

#Task4
list5 = list(range(0, 21, 2))
print(list5)

#Task5
list6 = list(range(0, 13))
list6.reverse()
print(list6)

#Task6
str_ = 'abcd1234'
list7 = list(str_)
print(list7)

#Task7
brand = 'Acer, HP, Lenovo, Asus, Honor, Apple, Toshiba, Samsung'
list8 = brand.split(', ')
print(list8)

#Task8
in1 = input('Введите числа через пробел: ')
list9 = in1.split(' ')
print(list9)

#Task9
in2 = input('Пишите название продуктов через _: ')
list10 = in2.split('_')
print(list10)

#Task10
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(list_[0])
print(list_[-2])
print(list_[1:-1])
print(list_[1::2])
print(list_[::-1])
print(list_[-2:0:-1])

#Task11
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_[1] = 200
print(list_)

#Task12
list_ = [1, 2, 3, 4, 5]
list_[-2:] = [12, 13]
print(list_)

#Task13
list_ = [1, 3, 5, 4, 7, 9, 8, 10, 1, 14, 19, 20]
print(max(list_))
print(min(list_))
print(len(list_))
print(sum(list_) / len(list_))

#Task14
brand = ['Acer', 'HP', 'Lenovo', 'Asus', 'Honor', 'Apple', 'Toshiba', 'Samsung']
res = brand.index('Honor')
print(res)

#Task15
brand = ['Acer', 'HP', 'Lenovo', 'Asus', 'Honor', 'Apple', 'Toshiba', 'Samsung']
res = brand.index('Apple')
brand[res] = 'irbis'
print(brand)

#Task16
brand = ['Acer', 'HP', 'Lenovo', 'Asus', 'Honor', 'Apple', 'Toshiba', 'Samsung']
price = [20000, 27000, 95000, 15000, 50000, 100000, 85000, 80000]
res = price.index(max(price))
print(brand[res])

#Task17
product_name = []
price = []
input_str = input('Введите название продукта и его цену через - : ')
a, b = input_str.split(' - ')
product_name.append(a)
price.append(int(b))
print(product_name, price)

#Task18
a = input('Введите меншьее число: ')
b = input('Введите большее число: ')
list_ = list(range(int(a), int(b)+1))
print(max(list_), min(list_))

#Task19
daily_list = [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1]
total_days = len(daily_list)
gut_day = daily_list.count(1)
shclecht_day = daily_list.count(0)
print(f'Всего дней: {total_days}, Хороших дней: {gut_day}, Плохих дней: {shclecht_day}')

#Task20
daily_list = [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1]
total_days = len(daily_list)
gut_day = daily_list.count(1)
res = (gut_day / total_days) * 100
print(f'Процент хороших дней: {res}%')

#Task21
dol_list = [70, 75, 80, 90, 90, 91, 90, 89, 100, 101, 95, 90, 89, 90, 91, 90, 90, 89, 92]
dol_list.sort()
print(dol_list)

#Task22
brand = ['Acer', 'HP', 'Lenovo', 'Honor']
input_str = input('Введите название бренда: ').lower()
if(input_str.capitalize() in brand):
    print('Бренд есть в списке')
else:
    brand.append(input_str.capitalize())
    print('Бренд добавлен в список', brand)

#Task23
a = input('Введите два числа через пробел: ')
num1, num2 = map(int, a.split(' '))
if(num1 < num2):
    list_ = list(range(int(num1), int(num2)+1))
elif(num1 > num2):
    list_ = list(range(int(num2), int(num1)+1))
else:
    list_ = [int(num1)]
print(list_)

#Task24
brand = ['Acer', 'HP', 'Lenovo', 'Asus', 'Honor', 'Apple', 'Toshiba', 'Samsung']
brand.remove('Honor')
print(brand)

#Task25
num_list = [1, 4, 2, 5, 3, 10, 2, 4]
num_list.remove(max(num_list))
print(num_list)

#Task26
brand = ['Acer', 'HP', 'Lenovo', 'Asus', 'Honor', 'Apple']
price = [20000, 27000, 95000, 15000, 50000, 90000]

input_ = input("Введите бренд и цену через '-': ")
name, cost = input_.split('-')
name = name.strip().title()
cost = int(cost.strip())

if name in brand:
    index = brand.index(name)
    if cost == 0:
        brand.reamove(name)
        price.pop(index)
    else:
        price[index] = cost
else:
    if cost != 0:
        brand.append(name)
        price.append(cost)

print(brand, price)

#Task27
nums = list(map(int, input('Введите числа через пробел: ').split()))
nums.sort()
n = len(nums)
if n%2 == 0:
    median = nums[n // 2]
else:
    median = (nums [n//2 - 1] + nums[n//2]) / 2
print(f'Медиана: {median}')

#Task28
a = [2, 6, 8, 3, 6, 1, 7, 4]
max = max(a)
min = min(a)
a[a.index(max)] = min
a[a.index(min)] = max
print(a)

#Task29
scores = list(map(int, input('Введите оценки через пробел: ').split()))
average = sum(scores) / len(scores)
if average > 85:
    print('Повыешенное стипендия')
elif 60 < average <= 85:
    print('Обычная стипендия')
else:
    print('Стипендия не предусмотрена')

#Task30
names_str = 'Айдана Жылдыз Бакыт Чолпон Мадина Жаныбек Алиса'
name = input('Введите имя:')
names_list = names_str.split(' ')
if(name in names_list):
    names_list.reamove(name)
    print('Имя удалено. Обновленный список:', names_list)
else:
    names_list.append(name)
    print('Имя добавлено. Обновленный список:', names_list)
