# Координатные четверти
# Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество 
# точек, лежащих в каждой координатной четверти.
# 
# Формат входных данных
# В первой строке записано количество точек. Каждая следующая строка состоит из двух 
# целых чисел — координат точки (сначала абсцисса – x, затем ордината – y), разделенных 
# символом пробела.
# 
# Формат выходных данных
# Программа должна вывести количество точек, лежащих в каждой координатной четверти, 
# как в примерах.
# 
# Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к 
# какой-либо координатной четверти.



def coordinate_quarters(total):
    x_y = []
    x_y_dig = []
    count_quarter_1 = 0
    count_quarter_2 = 0
    count_quarter_3 = 0
    count_quarter_4 = 0
    for i in range(total):
        x_y.append(input().split(" "))
#    print(x_y, int(x_y[i][0]), int(x_y[i][1]))
#    print(x_y[0])
    for item in x_y:
        if int(item[0]) == 0 or int(item[1]) == 0:
            continue
        elif int(item[0]) > 0 and int(item[1]) > 0:
            count_quarter_1 += 1
        elif int(item[0]) < 0 and int(item[1]) > 0:
            count_quarter_2 += 1
        elif int(item[0]) < 0 and int(item[1]) < 0:
            count_quarter_3 += 1
        elif int(item[0]) > 0 and int(item[1]) < 0:
            count_quarter_4 += 1

    print("Первая четверть:", count_quarter_1)
    print("Вторая четверть:", count_quarter_2)
    print("Третья четверть:", count_quarter_3)
    print("Четвертая четверть:", count_quarter_4)
    
coordinate_quarters(int(input()))