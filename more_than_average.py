'''
Больше среднего

Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, 
больших среднего арифметического элементов данной строки.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем 
элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести n чисел – для каждой строки количество элементов матрицы, больших среднего 
арифметического элементов данной строки.

Тестовые данные 🟢

Sample Input 1:
4
1 2 3 4
5 6 3 15
0 2 3 1
5 2 8 5

Sample Output 1:
2
1
2
1

Sample Input 2:
2
5 6
99 5

Sample Output 2:
1
1

Sample Input 3:
3
666 666 666
777 777 777
100 100 100

Sample Output 3:
0
0
0
'''

def matrix():
    n = int(input())
    matrix = []
    for i in range(n):
        row = [int(num) for num in input().split()]
        matrix.append(row)
    return matrix

def average_row(row):
    sum_row = 0
    count = 0
    for num in row:
        sum_row += num
        count += 1
    average = sum_row / count
    return average

def count_greater_than_average(row):
    average = average_row(row)
    count = 0
    for num in row:
        if num > average:
            count += 1
    return count

# Создаем матрицу
matrix_data = matrix()

# Выводим количество элементов в каждой строке, больших среднего арифметического
for row in matrix_data:
    average_value = average_row(row)
    greater_count = count_greater_than_average(row)
    print(greater_count)

