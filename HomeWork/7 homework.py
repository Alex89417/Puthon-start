""" # Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько 
# легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке
# Ввод:                                                           Вывод:
#     пара-ра-рам рам-пам-папам па-ра-па-дам                           Парам пам-пам

stroka = input("Введите стих для проверки: ")
stroka = stroka.split()
if len(stroka) < 2:
    print("Количество фраз должно быть больше одной!")
else:
    gl = "аоуыэеёиюя"
    new = set()
    for i in stroka:
        new.add(len(list(filter(lambda x: x in gl, i))))
    if len(new) == 1:
        print("Парам пам-пам")
    else: 
        print("Пам парам") """


""" # Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть 
# распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.
# Ввод:                                                                               Вывод:
# print_operation_table(lambda x, y: x * y)                                                       1 2 3 4 5 6
#                                                                                                 2 4 6 8 10 12
#                                                                                                 3 6 9 12 15 18
#                                                                                                 4 8 12 16 20 24
#                                                                                                 5 10 15 20 25 30
#                                                                                                 6 12 18 24 30 36 


def print_operation_table(op, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    else:
        for i in range(1, num_rows + 1):
            res = list()
            for j in range(1, num_columns + 1):
                if i == 1: res.append(j)
                elif j == 1: res.append(i)
                else:
                    res.append(op(i, j))
            print(*res)

print_operation_table(lambda x, y: x + y, 6, 6) """




# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть 
# распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.
# Ввод:                                                                               Вывод:
# print_operation_table(lambda x, y: x * y)                                                       1 2 3 4 5 6
#                                                                                                 2 4 6 8 10 12
#                                                                                                 3 6 9 12 15 18
#                                                                                                 4 8 12 16 20 24
#                                                                                                 5 10 15 20 25 30
#                                                                                                 6 12 18 24 30 36 

""" def print_operation_table(operation,num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print("Ошибка")
    else:
        for i in range(num_rows):
            for j in range(num_columns):
               
                print(operation(i, j), end = " ")
            print()


print_operation_table(lambda x, y: x * y, 6, 6) """


