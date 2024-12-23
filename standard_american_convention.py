# Standard American Convention
# На вход программе подается натуральное число. Напишите программу, которая вставляет 
# в заданное число запятые в соответствии со стандартным американским соглашением о 
# запятых в больших числах.
# 
# Формат входных данных
# На вход программе подается натуральное число  n (0 < n < 10**100).
# 
# Формат выходных данных
# Программа должна вывести число с запятыми в соответствии с условием задачи.


while True:
    try:
        number = int(input("Введите натуральное число: "))
        if 0 <= number < 1000:
            print(number)
        elif number > 999:
            # Преобразуем число в строку и разбиваем на цифры
            number_str = str(number)
            convent_number_list = []
            
            # Добавляем цифры в список
            for i in range(0, len(number_str)):
                convent_number_list.append(int(number_str[i]))
            print(convent_number_list)
            # Добавляем запятые в соответствии с правилами
            if len(number_str) > 3:
                # Добавляем запятые каждые три цифры, кроме первой цифры
                for i in range(len(number_str), 0, -3):
                    if i != 0:
                        convent_number_list.insert(i, ",")
            
            # Преобразуем список обратно в строку
            convent_number_str = ''.join(map(str, convent_number_list))[0:-1]
            print(convent_number_str)
        else:
            print("Отрицательное число не подходит")
        break
    except ValueError:
        print("Ошибка! Введите число.")
