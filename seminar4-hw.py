#Task1
list_ = [10, 20, 30, 40, 50]
list2 = list_[2]
print(list2)

#Task2
list2 = [23, 34, 12, 7, 0, -4, -56, -100, 344, 98, 232]
list2.sort()
mid = len(list2) // 2
list2.pop(mid)
print(list2)

#Task3
list_ = [1, 22, 3, 45, 22, 4, 89, 87, 87, 4]
num = int(input('Введите число: '))
if num in list_:
    res = list_.count(num)
    print(f'Число {num} встречается {res} раз(а)')
else:
    print(f'Число {num} не найдено в списке')

#Task4
list_fruit = []
list_fruit.append('apple')
list_fruit.append('banana')
list_fruit.append('orange')
list_fruit.append('grape')
list_fruit.append('kiwi')
list_fruit[2] = 'mango'
print(list_fruit)

#Task5
nums = list(range(0, 20))
print(nums)

#Task6
ls1 = [3, 7, 1, 9]
ls2 = [4, 2, 8, 6]
ls3 = ls1 + ls2
list6 = sum(ls3)
print(list6)

#Task7
list_ = [1, 2, 3, 10, 100, 12, 4]
list9 = list(filter(lambda x: x > 10, list_))
print(list9)

#Task8
str = 'The second type of coordinate system is a projected coordinate system.'
list_ = list(str.split())
print(list_)