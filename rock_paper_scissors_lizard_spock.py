""" Камень, ножницы, бумага, ящерица, Спок 🌶️
Проиграв 10 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил 
усложнить игру. Теперь Тимур и Руслан играют в игру Камень, ножницы, бумага, 
ящерица, Спок. Помогите ребятам вновь бросить честный жребий и определить, кто 
будет делать следующий модуль в новом курсе.

Формат входных данных
На вход программе подаются две строки текста, содержащие по одному слову из 
перечня "камень", "ножницы", "бумага", "ящерица" или "Спок". На первой строке 
записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьевки: кто победил - Тимур или Руслан, 
или они сыграли вничью.

Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает 
камень. Камень давит ящерицу, а ящерица травит Спока, в то время как Спок ломает 
ножницы, которые, в свою очередь, отрезают голову ящерице, которая ест бумагу, на 
которой улики против Спока. Спок испаряет камень, а камень, разумеется, затупляет 
ножницы. """

person_1 = "Тимур"
person_2 = "Руслан"

input_person_1 = input().lower()
input_person_2 = input().lower()

elements = ["камень", "ножницы", "бумага", "ящерица", "спок"]

if input_person_1 == input_person_2:
    print("ничья")
else:
    if (input_person_1 == elements[4] and input_person_2 == elements[1]) or\
    (input_person_1 == elements[4] and input_person_2 == elements[0]):
        print(person_1)        
    elif (input_person_1 == elements[3] and input_person_2 == elements[4]) or\
    (input_person_1 == elements[3] and input_person_2 == elements[2]):
        print(person_1)
    elif (input_person_1 == elements[2] and input_person_2 == elements[4]) or\
    (input_person_1 == elements[2] and input_person_2 == elements[0]):
        print(person_1)
    elif (input_person_1 == elements[1] and input_person_2 == elements[3]) or\
    (input_person_1 == elements[1] and input_person_2 == elements[2]):
        print(person_1)
    elif (input_person_1 == elements[0] and input_person_2 == elements[3]) or\
    (input_person_1 == elements[0] and input_person_2 == elements[1]):
        print(person_1)
    else:
        print(person_2)