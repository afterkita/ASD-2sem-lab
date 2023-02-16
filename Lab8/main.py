import math
def Over_read():
    N = 0
    with open('input.txt', 'r') as f:
        for s in f:
            N += 1
    arr = []
    with open('input.txt', 'r') as f1:
        for s in f1:
            arr.append(s)
    for i in range(len(arr)):
        arr[i] = arr[i].split()
    return arr
def After_read(arr):
    knot_link = [] #Массив связей
    # Формирование массива связей
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if int(arr[i][j]) != 0:
                knot_link.append([i,j,int(arr[i][j])])
    #Очистка массива связей
    l = len(knot_link)
    for i in range(l):
        for j in range(l):
            if int(knot_link[i][0]) == int(knot_link[j][1]) and int(knot_link[i][1]) == int(knot_link[j][0]) and i != j:
                knot_link[i] = [0,0,0]
    l = len(knot_link)
    l1 = 0
    while True:
        if l1 >= len(knot_link):
            break
        if knot_link[l1] == [0,0,0]:
            knot_link.pop(l1)
        else:
            l1+=1
    return knot_link
def alg_Deikstr(n,arr):
    viset = [] # массив индексов посещённых элементов
    end_arr = [math.inf]*len(arr) # массив длин дорог до элементов
    end_arr[n] = 0

    while len(viset) != len(arr):
        con = math.inf
        con_i = 0
        # Нашли минимальную не посещённую метку метку
        for i in range(len(end_arr)):
            if i not in viset:
                if con>end_arr[i]:
                    con = end_arr[i]
                    con_i = i
        #print(con_i)
        viset.append(con_i)
        #print(arr[con_i])
        # Заменяем значения у не посещённых точек, если путь до них меньше указанного
        for i in range(len(arr[con_i])):
            if int(arr[con_i][i]) != 0:
                if i not in viset:
                    if end_arr[i] > int(arr[con_i][i])+end_arr[con_i]:
                        end_arr[i] = int(arr[con_i][i])+end_arr[con_i]
    return end_arr
# Todo Дописать алгорим Беллмана-Форда
def alg_Bellmana_Forda(n,arr):
    # Инициализируем массив растояний
    A = []
    for i in range(len(arr)):
        A.append([math.inf]*len(arr))
    A[n][n] = 0

    # Создаём массив связей
    link = After_read(arr)
    return link


print(alg_Deikstr(0,Over_read()))
#print(alg_Bellmana_Forda(0,Over_read()))

