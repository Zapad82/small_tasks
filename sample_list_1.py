'''
Список по образцу 1

На вход программе подается число n. Напишите программу, которая создает и выводит 
построчно список, состоящий из n списков 
[[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести построчно указанный список.

Тестовые данные 🟢
Sample Input 1:
3
Sample Output 1:
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]

Sample Input 2:
2
Sample Output 2:
[1, 2]
[1, 2]

Sample Input 3:
5
Sample Output 3:
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
'''

n = int(input())

k = [i for i in range(1, n+1)]

for i in range(n):
    print(k)