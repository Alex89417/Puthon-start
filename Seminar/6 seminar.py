""" # Задача № 37. Решение в группах: Дано натуральное число N и последовательность из N элементов. Требуется вывести эту 
# последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3

n = int(input("Введите размер массива: "))
def rotate(n):
    if n == 0:
        return "+"
    num = input("Введите число: ")
    return num + (rotate(n - 1))

print(rotate(n)) """


""" # Решение в группах: C помощью рекурсии проверить аргумент на палиндром:

n = input("Введите аргумент для проверки на ралиндром")

def palindrom(n):
    print(n)
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    return palindrom(n[1 : -1])

print(palindrom(n)) """


""" # Задача No45. Решение в группах: Два различных натуральных числа n и m называются дружественными, если сумма делителей 
# числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k 
# выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, 
# не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз 
# (перестановка чисел новую пару не дает).
# Ввод:          Вывод:
#     300             220 284

s = []

for i in range(1, 5000):
    sum1 = 0
    for j in range(1, i//2+1):
        if i%j == 0:
            sum1 += j
    s.append([i, sum1])
# print(s)
for p in range(len(s)):
    for b in range(p, len(s)):
        if p != b and s[b][0] == s[p][1] and s[b][1] == s[p][0]:
            print(s[b]) """



























