__author__ = 'Kirill Kosmachev'

#EASY

# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
km = int(input('введите кол-во километров: '))
def convert(km):
    miles = km / 1.609
    print(miles)
convert(km)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    celoe, drobnoe = number.split('.')
    my_drobnoe = drobnoe[0:ndigits]
    last_number = drobnoe[ndigits:ndigits+1]
    if last_number and int(last_number) > 4:
        my_drobnoe = my_drobnoe +1
    answer = celoe + '.' + str(my_drobnoe)
    return answer
number = input('number: ')
ndigits = int(input('ndigits: '))
answer = my_round(number, ndigits)
print(answer)

# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    if len(ticket_number) != 6:
        return False
    first_part = ticket_number[0:3]
    second_part = ticket_number[3:6]
    sum_first_part = 0
    for i in first_part:
        sum_first_part = sum_first_part + int(i)
    sum_second_part = 0
    for i in second_part:
        sum_second_part = sum_second_part + int(i)
    if sum_first_part == sum_second_part:
        return True
    else:
        return False
print(lucky_ticket('436751'))


# NORMAL 

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    f1 = 1
    f2 = 1
    i = 2
    fibonacci_sum1 = 0
    while i <= m:
        fibonacci_sum = f2 + f1
        f1 = f2
        f2 = fibonacci_sum
        i += 1
        if i == n-1:
            fibonacci_sum1 = fibonacci_sum

    return fibonacci_sum - fibonacci_sum1

print(fibonacci(7, 13))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1
    while n < len (origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_function(func,iterable):
    output_iterable = []
    for i in range(len(iterable)):
        if func(iterable[i]) == True:
            output_iterable.append(iterable[i])
    return output_iterable

func = lambda x: type(x) == str
iterable = [-1, 2, 'a', 4, 'fgf']
print(filter_function(func,iterable))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
from math import sqrt

print('Введите координаты точек в двумерной плоскости: \n'
      'А0(х0, у0), А1(х1, у1), А2(x2 ,у2), А3(x3 , у3))')
x = [int(input('x{} = '.format(x))) for x in range(0,4)]
y = [int(input('y{} = '.format(y))) for y in range(0,4)]

#Вариант1
sides = []
for i in range(0,4):

    if i == 3:
        side = [x[0] - x[i], y[0] - y[i]]
    else:
        side = [x[i + 1] - x[i], y[i + 1] - y[i]]

    sides.append(sqrt(side[0]**2 + side[1]**2))
print(sides)
if sides[0] == sides[2] and sides[1] == sides[3]:
    print('Точки являются вершинами параллелограмма')
else:
    print('Точки не являются вершинами параллелограмма')


#Вариант2
mid_diagonal1 = [(x[2] + x[0]) / 2, (y[2] + y[0]) / 2]
mid_diagonal2 = [(x[3] + x[1]) / 2, (y[3] + y[1]) / 2]

if mid_diagonal1 == mid_diagonal2:
    print('Точки являются вершинами параллелограмма')
else:
    print('Точки не являются вершинами параллелограмма')