""" Орел и решка
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". 
Буква "О" соответствует выпадению Орла, а буква "Р" – выпадению Решки. 
Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита 
"О" и "Р".

Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.

Примечание. Если выпавших Решек нет, то необходимо вывести число 0. """

input_text = input()
tail = "Р"
counter_tails = 0
max_tails = 0
for char in input_text:
    if char == tail:
        counter_tails += 1
    else:
        if counter_tails > max_tails:
            max_tails = counter_tails
        counter_tails = 0
    if counter_tails > max_tails:
        max_tails = counter_tails

print(max_tails)







