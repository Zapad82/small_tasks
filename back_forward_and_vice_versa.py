# Назад, вперед и наоборот ↔️
# На вход программе подается строка текста из натуральных чисел. Из элементов строки 
# формируется список чисел. Напишите программу, которая меняет местами соседние 
# элементы списка (a[0] c a[1], a[2] c a[3] и т.д.). Если в списке нечетное количество 
# элементов, то последний остается на своем месте.
# 
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные 
# пробелами.
# 
# Формат выходных данных
# Программа должна вывести измененный список, разделяя его элементы одним пробелом.

numbers_list = input().split(" ")

end = numbers_list[len(numbers_list)-1]
def new_numbers_list(numbers_list):
    new_numbers_list = []
    for i in range(0, len(numbers_list), 2):
        if i+1 == len(numbers_list):
            break
        else:
            numbers_list[i], numbers_list[i+1] = numbers_list[i+1], numbers_list[i]
            new_numbers_list.append(numbers_list[i])
            new_numbers_list.append(numbers_list[i+1])
    return new_numbers_list
if len(numbers_list) % 2 != 0:
    new_list = new_numbers_list(numbers_list) 
    new_list.append(end)
    print(*new_list, sep=" ")
else:
    print(*new_numbers_list(numbers_list), sep=" ")