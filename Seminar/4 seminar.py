""" # Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется 
# к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

stroka = "a a a b c a a d c d d".split()
slov = {}

# for i in stroka:
#     if i not in slov:
#         slov[i] = 1
#         print(i, end = " ")
#     else:
#         print(f"{i}_{slov[i]}", end = " ")
#         slov[i] += 1


for i in stroka:
    if i not in slov:
        print(i, end=" ")
    else:
        print(f"{i}_{slov[i]}", end=" ") 

    slov[i] = slov.get(i,0) + 1 """





