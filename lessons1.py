import math;

#task1
number = int(5)
number2 = int(10)
result = number + number2
print("The result is Task1:", result)


#task2
number3 = int(7)
number4 = int(2)
result2 = number3 // number4
print("The result of division is Task2:", result2)

#task3
number7 = int(15)
number8 = int(4)
result4 = number7 % number8
print("The remainder is Task3:", result4)

#task4
number9 = float(9.5)
number10 = float(2.5)
number11 = float(3.0)
result5 = number9 * number10 
result6 = result5 / number11
print("The final result is Task4:", result6)

#task5
number12 = float(5.0)
result7 = round((number12 ** number12) / 2, 1)
print("The final result is Task5:", result7)

#task6
number13 = float(8.0)
number14 = float(3.3)
result8 = math.floor(number13 - number14)
print("The final result is Task6:", result8)

#task7
number15 = float(8.0)
number16 = float(3.3)
result9 = math.ceil(number15 - number16)
print("The final result is Task7:", result9)

#task8
number17 = float(4)
number18 = float(5)
square1 = math.pow(number17, 2)
square2 = math.pow(number18, 2)
result10 = round((square1 + square2) ** 0.5, 2)
print("The final result is Task8:", result10)

#task9
number19 = int(25)
number20 = int(-5)
result11 = abs(number19) + abs(number20)
print("The final result is Task9:", result11)

#task10
temp = int(90)
result12 = round((temp - 32) * 5 / 9, 1)
print("The final result is Task10:", result12)

#task11
number21 = 6+7/12
number22 = 3+17/36
number23 = 4+1/3
number24 = 4/(1/4)-0.25
result13 = round(((number21 - number22)*2.5 - number23) / number24 / 0.65, 2)
print("The final result is Task11:", result13)

#taskk12 
number25 = ((( (2 + 3/4) / 1.1 + (3 + 1/3) ) / (5/7)) - (((2 + 1/6) + 4.5) * 0.375)) / (2.5 - 0.4 * (3 + 1/3))
result14 = round(number25, 3)
print("The final result is Task12:", result14)

#task13
number26 = ( (11 + 2/5) + (7 + 1/2) ) - ( (285.6 / 14 - (1 + 23/30) + 13/50) / (24.4 - 10.23) )
result15 = round(number26, 3)
print("The final result is Task13:", result15)

#task14
number27 = (((9 - (5 + 3/8)) * ((4 + 5/12) - (4 / (2 + 2/3))) + ((3/10) - (0.5 / 4)) * (4/7))/ ((1/24) + (0.25 / (13 + 1/3))))
result16 = round(number27, 3)
print("The final result is Task14:", result16)

#task15
number28 = 5.75 / 0.025
print("The final result is Task15:", number28)

#task16
number29 = ((0.16 * (3.2 - 3/40) + ((2 + 3/11) * 4.125 / (3 + 3/4))) / (((5 + 1/6) * 0.3) - (0.3 * 4.5) + ((1/3) * 0.3)))
result17 = round(number29 * 0.4, 3)
print("The final result is Task16:", result17)