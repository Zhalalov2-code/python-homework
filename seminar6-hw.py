#Task22
#У вас есть список со вложенными списками ls = [[0], [1, 2], [3, 5], [5, 6], [7, 8, 9]] выведите самый длинный список и самый короткий
ls = [[0], [1, 2], [3, 5], [5, 6], [7, 8, 9]]
longest = max(ls, key=len)
shortest = min(ls, key=len)
print("Самый длинный список:", longest)
print("Самый короткий список:", shortest)

#Task23
# #Дан список ls = [20, -40, 30, -20, 20, 30, 40, 50, 20, 60, 60, -70, -20] целых чисел с повторяющимися элементами. Вам надо создать еще один список task23, содержащий только повторяющиеся элементы
ls = [20, -40, 30, -20, 20, 30, 40, 50, 20, 60, 60, -70, -20]
task23 = list(set([x for x in ls if ls.count(x) > 1]))
print("Повторяющиеся элементы:", task23)

# Task24
nums = ['one', 'two', 'three', 'four', 'five']
task24 = [i[::-1] for i in nums]
print(task24)

# Task25
task25 = [[0, 2, 4, 5], [1, 2, 2, 8, 9], [3, 5, 3], [5, 6, 9, 12], [7, 82, 12, 9]]
res = [[j for j in i if j % 2 != 0] for i in task25]
print("Исходный список:", task25)
print("Без четных чисел:", res)

#Task26
#В списке ['one', 'two', 'three', 'four', 'five'] переведите все элементы в верхний регистр, ответ запишите в переменную task26
words = ['one', 'two', 'three', 'four', 'five']
task26 = [word.upper() for word in words]
print(task26)

#Task27
#Дан список целых чисел list_ = [2, 4, 97, 20, 10, 35, 23, 10, 1000] найдите минимальное значение, не используя встренную функцию min(), ответ запишите в переменную task27
list_ = [2, 4, 97, 20, 10, 35, 23, 10, 1000]
task27 = list_[0]
for num in list_:
    if num < task27:
        task27 = num
print(task27)

#Task28
#Найдите значение параметра, при котором система имеет одно единственное решение. Используйте итерации. Таких значений вы можете получить одно или два.
round_a = []
for a in range(-20, 20):
    D = (-(6+a))**2 - 4 * 1 * 1
    if D == 0:
        round_a.append(a)
print(round_a)

#Task29
import math
max_products = 0
for wL_a in range(101):
    wl_b = 100  - wL_a
    a1 = 3 * wL_a
    b1 = 1 * wl_b

    for w2_a in range(101):
        w2_n = 100 - w2_a
        a2 = int(math.sqrt(w2_a))
        b2 = int(math.sqrt(w2_n))

        total_a = a1 + a2
        total_b = b1 + b2

        products = min(total_a, total_b // 3)
        if products > max_products:
            max_products = products
print(f"Максимальное количество продуктов: {max_products}")