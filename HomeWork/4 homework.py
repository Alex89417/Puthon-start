""" # Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

#                                                                 1 вариант

import random

x = str(input("Введите два числа через пробел: ")).split()
var2 = [random.randint(1, 9) for k in range(int(x[0]))]
var3 = [random.randint(1, 9) for k in range(int(x[1]))]
list_1 = list()
print(var2)
print(var3)
for i in var2:
    if i in var3 and i not in list_1:
        list_1.append((i))
list_1.sort()
print(*list_1)


#                                                                 2 вариант

# import random

# x = str(input("Введите два числа через пробел: ")).split()
# var2 = [random.randint(1, 9) for k in range(int(x[0]))]
# var3 = [random.randint(1, 9) for k in range(int(x[1]))]
# print(var2)
# print(var3)
# print(*sorted(set(var2) & set(var3)))
 

#                                                                 3 вариант

# var_1 = {'1', '5', '3', '7', '9'}
# var_2 = {'2', '5', '3', '4'}
# lok = var_1 & var_2
# # i = var_1.intersection(var_2)
# j = list(lok)
# j.sort()
# print(*j)


#                                                                 вариант gb
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5'

# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)

# lok = set_1 & set_2
# print(lok)
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ') """


""" # Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход, 
# находясь перед некоторым кустом грядки.Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов.
# Входные данные:
# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым
# кустом грядки.

#                                                                 вариант 1

import random
a = int(input("Введите количество кустов: "))
arr = [random.randint(1, 20) for _ in range(a)]
sum = 0
for i in range(a):
   if (arr[i] + arr[i-1] + arr[i-2]) > sum:
      sum = (arr[i] + arr[i-1] + arr[i-2])  
print(arr)
print(sum)


#                                                                 вариант gb

# arr_count = list()
# for i in range(len(arr) - 1):
#    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])

# # Вывод максимальной урожайности, которую может собрать собирающий модуль
# print(max(arr_count))

# # немного подделанный!

# arr = [2, 4, 6, 8, 10]
# for i in range(len(arr) - 2):
#    arr.append(arr[i] + arr[i + 1] + arr[i + 2])
# print(max(arr)) """


