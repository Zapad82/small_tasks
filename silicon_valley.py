"""
Кремниевая долина 🤖🌶️🌶️
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных 
холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". 
Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв 
и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, 
главное наличие последовательности букв), то холодильник заражен и нужно вывести 
номер холодильника, нумерация начинается с единицы.

Формат входных данных
В первой строке подается число n – количество холодильников. В последующих n строках 
вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке 
от 5 до 100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. 
Если таких холодильников нет, ничего выводить не нужно.
"""

number_of_refrigerators = int(input())
list_of_refrigerators = [input() for i in range(number_of_refrigerators)]
list_of_attack = []
flag = False
for i in range(number_of_refrigerators):
    if "a" in list_of_refrigerators[i] and "n" in list_of_refrigerators[i] and "t" in list_of_refrigerators[i] and "o" in list_of_refrigerators[i]:
        flag = True
    else:
        continue
        
    if flag == True:
        if "n" in list_of_refrigerators[i][list_of_refrigerators[i].index("a")+1:] and "t" in list_of_refrigerators[i][list_of_refrigerators[i].index("a")+1:] and "o" in list_of_refrigerators[i][list_of_refrigerators[i].index("a")+1:]:
            flag = True
        else:
            continue   
            
    if flag == True:
        if "t" in list_of_refrigerators[i][list_of_refrigerators[i].index("n")+1:] and "n" in list_of_refrigerators[i][list_of_refrigerators[i].index("n")+1:] and "o" in list_of_refrigerators[i][list_of_refrigerators[i].index("n")+1:]:
            flag = True
        else:
            continue
            
    if flag == True:
        if "o" in list_of_refrigerators[i][list_of_refrigerators[i].index("t")+1:] and "n" in list_of_refrigerators[i][list_of_refrigerators[i].index("t")+1:]:
            flag = True
        else:
            continue
            
    if flag == True:
        if "n" in list_of_refrigerators[i][list_of_refrigerators[i].index("o")+1:]:
            flag = True
        else:
            continue


    list_of_attack.append(i+1)
print(*list_of_attack, sep=" ")
