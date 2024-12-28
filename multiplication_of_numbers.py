""" Произведение чисел
Напишите программу для определения, является ли число произведением двух чисел из 
данного набора. Программа должна выводить результат в виде ответа ДА или НЕТ.

Формат входных данных
В первой строке подается натуральное число n (1<n<1000) – количество чисел в наборе. 
В последующих n строках вводятся целые числа, составляющие набор (могут повторяться). 
Затем следует целое число, которое является или не является произведением двух 
каких-то чисел из набора.

Формат выходных данных
Программа должна вывести ДА или НЕТ в соответствии с условием задачи.

Примечание 1. Само на себя число из набора умножиться не может. Другими словами, 
два множителя должны иметь разные индексы в наборе.

Примечание 2. Для решения задачи используйте вложенные циклы. """

n = int(input())

numbers_list = [int(input()) for i in range(n)]
result_number = int(input())
flag = False
for i in range(len(numbers_list)):
    for j in range(len(numbers_list)):
        if i != j:
            if numbers_list[i] * numbers_list[j] == result_number:
                flag = True
                break

if flag == True:
    print("ДА")
else:
    print("НЕТ")