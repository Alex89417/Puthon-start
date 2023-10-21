""" # Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
# n=16
#Вывод 1, 2, 4, 8, 16
n = int(input("Введите число кратное 2: "))
i = 2
m = 1
while m <= n:
    print(m)
    m += m
    i += 2
    
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1 """

""" # Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В результате вы должны вывести все возможные 
# варианты чисел X и Y через пробел.

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

for i in range(1, s):
    if s - i == p/i:
        print(i, int(p/i))


# for x in range(s + 1):
#     for y in range(s + 1):
#         if x + y == s and x * y == p:
#             print(x, y)


# x = 1
# while x < s:
#     y = 1
#     while y < s:
#         if x + y == s and x * y == p:
#             print(x, y)
#         y += 1
#     x += 1 """
    
""" coins = input("Введите число: ")

#coins = [0, 1, 0, 1, 1, 1, 0]
c = 0
c1 = 0
i = 0
while i < len(coins):
    if int(coins[i]) == 1: 
        c += 1
    if int(coins[i]) == 0: 
        c1 += 1
    i += 1
if c > c1: print(c1)
else: print(c) 


# coins = [0, 1, 0, 1, 1, 1, 0, 0]
# count = 0
# for i in coins:
#     if i == 0:
#         count+=1

# if len(coins) - count < count:
#     print(len(coins) - count)

# else:print(count)"""

""" # # Орел и решка
# # Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует 
# # выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# # Формат входных данных:  На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# # ОРРОРОРООРРРО
# # Output: 3

#                                                      1
# money = "OPPPPPPOPOPOOPPPOPPPPP"
# count = 0
# list1 = list()

# for i in money:
#     if i == "P":
#         count += 1
#     elif i != "P" and count > 0:
#         list1.append(count)
#         count = 0

# if count > 0: list1.append(count)
# print(list1)

# maxEl = 0
# for i in list1:
#     if i > maxEl:
#         maxEl = i
# print(maxEl)


#                                                      2
# money = "OPPPPPPOPOPOOPPPOPPPPP"
# count = 0
# count1 = 0

# for i in money:
#     if i == "P":
#         count += 1
#     elif i != "P":
#         if count > count1:
#             count1 = count
#         count = 0

# if count > count1:
#     count1 = count
# print (count1)


#                                                      3
money = "OPPPOPOPOOPPPOPPPPP"
n = 0
while "P" * n in money:
    n += 1

print(n - 1) """








