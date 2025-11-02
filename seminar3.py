#Task1
a = 3
b = 5.3
c = True

result = str(a) + "-" + str(b) + "-" + str(c)
print(result)
print(type(result))

#Task2
a = str(input("Напишите что-нибудь: "))
print(a)

#Task3+Task4
a = str(input('Write your name: '))
b = str(input('Write your surname: '))
res = a + " " + b
print(res)

#Task5
text = 'Hello, [name]! Your score is [score].'
name = input('Enter your name: ')
score = input('Enter your score: ')
res  = text.replace('[name]', name).replace('[score]', score)
print(res)

#Task6
text = "Меня зовут [name], и мне [age] лет."
name = str(input("Введите ваше имя: "))
age = str(input("Введите ваш возраст: "))
res = text.replace('[name]', name).replace('[age]', age)
print(res)

#Task7
text = 'python is easy'
s = text[0:1]
s = text[13:]
s = text[0:2]
s = text[10:]
s = text[2:4]
s = text[1:7]
s = text[1:12]
s = text[1:13]
s = text[0:14]
s = text[1:14]
s = text[-1: -14]
s = text[-14: -1]
s = text[5: 4: 3]
s = text[:: -1]
print(s)

#Task8
text = "PythonProgrammingLanguage"
a = text[0:6]
b = text[6:17]
c = text[17:24]
res = a + " " + b + " " + c
print(res)

#Task9
text = "I am learning Python programming"
a = text[14:20]
b = 'java'
res = text.replace(a, b)
print(res)

#Task10
text = 'Hey, [name]'
name = input('Enter your name: ')
res = text.replace('[name]', name.capitalize())
print(res)

#Task11
code = 'atgcaagttgacaattta'
res = code.upper()
print(res)

#Task12
code = 'augcaagugacaauuua'
res = code.replace('u', 't')
print(res)

#Task13
number = '   +7(919)-@784-54_18@@     '
res = number.strip(' @-_()')

print(res)
#Task14
str = '67dg#uin_87'
res = len(str)
res1 = str.index('#')
print(res, res1)

#Task15
text = """ Имя этого героя "name". Поход в театр для него целый ритуал. Входя в фойе, "name" демонстративно снимает шляпу, поправляет галстук и вешает
ольто на руку. Он непременно думает, что все, кому он знаком говорят про себя: "Ах, сегодня "name" неотразим!" После чего "name"
занимает лучшее место бенуара и с важным видом достает очки."""
name = input('Введите имя героя: ')
res = text.replace('"name"', name)
print(res)

#Task16
str = '84hj#55hjl'
abc = 'abc'
res = len(str)
res1 = str[:5].replace(abc, '')
print(res, res1)

#Task17
number = "+996 (nnn) nnn-nnn"
tel = '0777784500'
res = number.replace('nnn', tel[1:4]).replace("nnn", tel[4:7]).replace('nnn', tel[7:10])
print(res)

#Task18
str = input("Введите строку: ")
res = len(str) > 5 and 'too long'
print(res)


#Task19
text = input("Введите строку: ")
res = len(text) < 5 and input("too long, попробуйте снова: ") or text
print(res)

#Task20andTask21
password = input("Введите пароль: ")
res = len(password) >= 8 and any(ch in password for ch in '!@#$%^&*()-_=+[]{};:,.<>?/') and "Сильный пароль" or input("Введите пароль еще раз, он должен быть больше 8 символов и содержать @#>.,: ")
res1 = len(password) >= 8 and any(ch in password for ch in '!@#$%^&*()-_=+[]{};:,.<>?/') and 'Пароль принят' or 'Пароль не принят'
print(res1)

#Task22
name_list = 'айданургулсайкалаймээржылдызбакытайчолпонмадинажаныбекбекжолдостукэлиябатыржанаталмазбекчингизталанталтынбекмаратсаматтайырбеказаматбек'
name = input("Введите имя: ").lower()
res = name in name_list and 'Поздравляю, вам положена повышенная стипендия.' or 'Увы, Вашего имени в списке нет'
print(res)

#Task23
code = 'GGGGGGGGGAATTATGATCCTTACTTT'
res = code[0] == "G" and "A" + code[1:0] or code
g_count = code.count('G')
res1 = (g_count < 5 and code + 3 * 'G') or code
print(res, g_count, res1)

#Task24
names = input("Введите два имени через пробел: ")
res = names.replace(' ', ' \n')
print(res)

#Task25
prod_name = str(input("Введите название товаров: "))
old_price = int(input("Введите старую цену: "))
new_price = int(input("Введите новую цену: "))
text = 'Товар [name] подорожал на [precent]%'
precent = ((new_price - old_price) / old_price) * 100
res = text.replace('[name]', prod_name).replace('[precent]', str(round(precent, 2)))
print(res)

#Task26
text = 'Helo'
res = (len(text) > 2 and text[0] + text[1:-1][::-1] + text[-1]) or text
print(res)

#Task27
text = '      съешь ещё этих мягких французских булок, да выпей чаю      '
text_count = text.strip().count(' ') + 1
print(text_count)

#Task28
text = 'sksjhkjn23456kjhkjhkxcv1234'
sum = len(text)
mid = (sum + 1) // 2
res = text[mid:] + text[:mid]
print(res)

#Task29
text = 'разделяем строку'
a, b = text.split(' ')
res = b + ' ' + a
print(res)

#Task30
text = 'sksjhkjn23456kjhkjffhkxcv12ffff34'
count_f = text.count('f')
res = (
    (count_f == 1 and text.index('f')) or
    (count_f >= 2 and f"{text.index('f')} {text.rindex('f')}")
)
res and print(res)

#Task31
text = '09drh121985fh0u91'
first_h = text.index('h')
last_h = text.rindex('h')
res = text[:first_h +1] + text[last_h:]
print(res)

#Task32
text = "Engagementeng" 
res = (
    (text[:3].lower() == text[-3:].lower() and text[::-1])
    or text
)
print(res)

#Task33
bad_goods = ['сигареты', 'пиво', 'вино', 'водка', 'коньяк']
goods = input("Что покупаете (через пробел): ").lower().strip()
need_age = any(item in goods.split() for item in bad_goods)
age = need_age and int(input("Сколько вам лет? ")) < 18 and "Товар не продадим вам меньше 18" or "Товар продадим вам больше 18"
print(age)

#Task34
print("Введите данные двух студентов.")

name1 = input("Имя 1-го: ").strip()
math1 = int(input(f"Math для {name1}: "))
eng1 = int(input(f"English для {name1}: "))

name2 = input("Имя 2-го: ").strip()
math2 = int(input(f"Math для {name2}: "))
eng2 = int(input(f"English для {name2}: "))

avg1 = (math1 + eng1) / 2
avg2 = (math2 + eng2) / 2

print()
print(f"{'':10} {'Math':>6} {'English':>8} {'Avg':>6}")
print(f"{name1:10} {math1:6} {eng1:8} {avg1:6.1f}")
print(f"{name2:10} {math2:6} {eng2:8} {avg2:6.1f}")

#Task35
brand_str = 'Acer, Asus, Honor, HP, Lenovo'
price_str = '20 000, 35 000, 50 000, 40 000, 25 000'

brands = [b.strip() for b in brand_str.split(',')]
prices = [int(p.strip().replace(' ', '')) for p in price_str.split(',')]

catalog = dict(zip(brands, prices))

user_brand = input("Введите бренд: ").strip()

base_price = catalog.get(user_brand)
(
    base_price
    and (
        print(f"{user_brand}:"),
        print(f"    i3: {base_price:,} сом.".replace(',', ' ')),
        print(f"    i5: {int(base_price * 1.20):,} сом.".replace(',', ' ')),
        print(f"    i7: {int(base_price * 1.45):,} сом.".replace(',', ' '))
    )
) or (base_price is None and print("Такого бренда нет в наличии."))

#Task36
A = input('Write A coords (x y): ').strip()
B = input('Write B coords (x y): ').strip()

has_space = (' ' in A) and (' ' in B)

has_space or print("❌ Ошибка: координаты должны быть через пробел.")

coordsA = has_space and A.split()
coordsB = has_space and B.split()

x1 = has_space and float(coordsA[0])
y1 = has_space and float(coordsA[1])
x2 = has_space and float(coordsB[0])
y2 = has_space and float(coordsB[1])

not_vertical = has_space and (x1 != x2)

(has_space and not not_vertical) and print("❌ Невозможно вычислить k: x1 == x2")

(not_vertical) and (
    (k := (y2 - y1) / (x2 - x1)),
    (b := y1 - k * x1),
    print("✅ Ввод корректен."),
    print(f"k = {k}"),
    print(f"b = {b}"),
    print(f"y = {k} * x + {b}")
)
