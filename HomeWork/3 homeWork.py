""" # Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 3
#  1

list_1 = [1, 2, 3, 2, 3, 2, 4, 4, 3]
k = 3
# c = 0
# i = 0
# while i < len(list_1):
#     if list_1[i] == k:
#         c += 1
#     i += 1
# print(c)


# count = 0
# for i in list_1:
#     if i == k:
#         count += 1
# print(count)

print(list_1.count(k)) """


""" # Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Пример:
list_1 = [1, 2, 3, 4, 8]
k = 7

a = abs(k - list_1[0])
num = list_1[0]
for i in range(1, len(list_1)):
    if a > abs(list_1[i] - k):
        a = abs(list_1[i] - k)
        num = list_1[i]
print(num) """


"""# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, 
# что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

k = "НОУТБУК"
k = k.upper()
dictionary = {"AEIOULNSTRАВЕИНОРСТ" : 1, "DGДКЛМПУ " : 2, "BCMPБГЁЬЯ" : 3, "FHVWYЙЫ" : 4, "KЖЗХЦЧ" : 5, "JXШЭЮ" : 8, "QZФЩЪ" : 10}
sum = 0
for i in k:
    for j in dictionary:
        if i in j:
            sum += dictionary[j]
print(sum) """





