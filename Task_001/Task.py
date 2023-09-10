# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

def Random_list(len, left_range, right_range):
    from random import randint

    numbers = []
    for i in range(len):
        numbers.append(randint(left_range, right_range))
    return numbers

# len_1 = 15
# len_2 = 20
# left_range_1 = 0
# right_range_1 = 10
# left_range_2 = 0
# right_range_2 = 10
len_1 = int(input('Введите количество элементов первого списка: '))
len_2 = int(input('Введите количество элементов второго списка: '))
left_range_1 = int(input('Введите наименьший элемент первого списка: '))
right_range_1 = int(input('Введите наибольший элемент первого списка: '))
left_range_2 = int(input('Введите наименший элемент второго списка: '))
right_range_2 = int(input('Введите наибольший элемент второго списка: '))

list_1 = Random_list(len_1, left_range_1, right_range_1)
list_2 = Random_list(len_2, left_range_2, right_range_2)
list_3 = []
i = 0
if len_1 < len_2:
    min = len_1
    while i < min:
        if list_1[i] in list_2:
            list_3.append(list_1[i])
            i += 1
        else:
            i += 1
else:
    min = len_2
    while i < min:
        if list_2[i] in list_1:
            list_3.append(list_2[i])
            i += 1
        else:
            i += 1

# print (list_3)
list_4 = list(set(list_3))
list_4.sort()
print (list_4)
