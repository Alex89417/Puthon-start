""" # Задача №31. Решение в группах: Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21


def fib(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

k = int(input("Введите число: "))
print (fib(k)) """ 


""" # Задача №33. Решение в группах: Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# -------------------------------   1   --------------------------------------
# list1 = [1, 3, 3, 3, 4]
# min_el = list1[0]
# max_el = list1[0]

# for i in range(len(list1)):
#     if list1[i] > max_el:
#         max_el = list1[i]
#     if list1[i] < min_el:
#         min_el = list1[i] 

# for i in range(len(list1)):
#     if list1[i] == max_el:
#         list1[i] = min_el

# print(list1)

# ------------------------------    2   --------------------------------------
# list1 = [1, 3, 3, 3, 4]
# min_el = min(list1)
# max_el = max(list1)

# for i in range(len(list1)):
#     if list1[i] == max_el:
#         list1[i] = min_el

# print(list1) """


""" # Задача №35. Решение в группах: Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

n = int(input("Введите проверочное число: "))

def simpl_num(n, z = 2):
    if n == 2 or z * z > n:
        return True
    elif n % z == 0:
        return False
    return simpl_num(n, z + 1)

print(simpl_num(n)) """




#-----------------------------------------   мой вариант,  ---------------------------------------
# n = int(input("Введите цифру: "))
# count = 0
# for i in range(1, 10):
#     if n % i == 0:
#         count += 1

# if count == 2:
#     print("Yes")
# else: 
#     print("No")






# ===================================================================
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1 )
    

# print(factorial(5))


# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(6))