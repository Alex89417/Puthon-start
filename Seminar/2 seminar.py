""" # По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input:       5
# Output:    120

# n = int(input("Введите число: "))

# i = 1
# sum = 1
# while i < n:
#     sum *= (i + 1)
#     i += 1
# print(sum)


n = int(input("Введите целое неотрицательное число \n"))
fact = 1
while n > 0:
    fact *= n
    n -= 1

print(fact) """


""" # Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, 
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input:     5
# Output:  6

n = int(input("Введите целое число больше 1: "))

fib1 = 1
fib2 = 1
fib3 = 1
i = 4

while fib3 < n:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    if fib3 == n: 
        print(i)  
    elif fib3 > n:
        print(-1)
    i += 1

if n == 1: 
    print(2, 3) """







""" Орел и решка

Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.

Примечание. Если выпавших Решек нет, то необходимо вывести число 
0
0.

Тестовые данные 🟢
Sample Input 1:
ОРРОРОРООРРРО
Sample Output 1:
3
Sample Input 2:
ООООООРРРОРОРРРРРРР
Sample Output 2:
7
Sample Input 3:
ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
Sample Output 3:
31 """








