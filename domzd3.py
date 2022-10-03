__author__ = 'Kirill Kosmahev'

# EASY

# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: использует метод .format()
lst = ["яблоко", "банан", "киви", "арбуз"]
maxlen = 0
for i in lst:
    if len(i) > maxlen:
        maxlen = len(i)
for i in range(len(lst)):
    print(("{0}. {1:>" + str(maxlen) + "}").format(i + 1, lst[i]))
print()

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.

lst1 = [1, 3, 5, 7, 9]
lst2 = [3, 8, 6, 5]
res = []
print(lst1, lst2)
for i in lst1:
    if i not in lst2:
        res.append(i)
lst1 = res
print(lst1, lst2)
print()

# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

lst = [1, 4, 3, 42, 48, 34, 4, 5, 10, 7, 8, 9]
res = []
print(lst)
for i in lst:
    if i % 2 == 0:
        res.append(int(i / 4))
    else:
        res.append(i * 2)
print(res)

# вариант 2
def prepare(item):
    return int(item / 4) if item % 2 == 0 else item * 2

res2 = list(map(prepare, lst))
print(res2) 

#NORMAL 

__author__ = 'Шварева Софья Дмитриевна'
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

from math import sqrt, modf
from random import randint

list1 = [randint(-10, 100) for i in range(10)]
list2 = []

for number in list1:
    if number >= 0:
        square_root = sqrt(number)
        aaa = modf(square_root)
        #print(aaa)
        if square_root == aaa[1]:
            list2.append(int(square_root))

print('Исходный список: ', list1, '; Новый список: ', list2)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# date = input('Введите дату в формате dd.mm.yyyy: ')
date = '02.11.2013'
d = date.split('.')
day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое',
       '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое', '12': 'двенадцатое',
       '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое',
       '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое',
       '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое',
       '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое',
       '30': 'тридцатое', '31': 'тридцать первое'}
month = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
         '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
print('Дата', date, 'в текстовом виде: ')
print(day.get(d[0]), month.get(d[1]), d[2], 'года')


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

#n = int(input('Введите длину списка n : '))
n = 10

list3 = [randint(-100, 100) for ii in range(n)]
print('Случайный список:', list3)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [randint(0, 20) for iii in range(10)]
print('Исходный список: ', lst)
lst2 = []
for element in lst:
    if element not in lst2:
        lst2.append(element)
print('Неповторяющиеся элементы исходного списка: ', lst2)

lst3 = []
for element in lst:
    if lst.count(element) == 1:
        lst3.append(element)
print('Элементы исходного списка, которые не имеют повторений: ', lst3)