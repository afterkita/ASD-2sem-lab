import math
# ToDo Решение не верное как и статья в википедии
#Алгоритм был предложен Флёри в 1883 году.
#Пусть задан граф G=(V,E). Начинаем с некоторой вершины V и каждый раз вычеркиваем пройденное ребро.
# Не проходим по ребру, если удаление этого ребра приводит к разбиению графа на две связные компоненты (не считая изолированных вершин),
# т.е. необходимо проверять, является ли ребро мостом или нет.
# Заполнение массива по матрице путей
def Graf_go(s):
    N = 0
    with open( s+'.txt', 'r') as f:
        for s in f:
            N += 1
    arr = []
    with open('input.txt', 'r') as f1:
        for s in f1:
            arr.append(s)
    for i in range(len(arr)):
        arr[i] = arr[i].split()
    return arr
# Заполнение массива по матрице путей

def BFS_Svaz(s):
    # Заполнение массива
    arr = Graf_go(s)
    Out_arr = []

    # Просматриваем все точки на предмет связанности
    for i in range(len(arr)):
        viset = []
        qer = []
        co = False
        for j in range(len(Out_arr)):
            if arr[i] in Out_arr[j]:
                co = True
        if co == False:
            viset.append(arr[i])
            # Заполнение очереди для первой точки алгоритма
            for k in range(len(arr)):
                if int(arr[i][k]) > 0:
                    if arr[k] not in viset:
                        qer.append(k)
            BFS_Krec(arr, qer, viset)
            Out_arr.append(viset)
        Out_arr.append(viset)

    # Обработка массива
    for u in range(len(Out_arr)):
        if u%2 != 0:
            Out_arr[u]=[]
    for u in range(len(Out_arr)-1,0,-1):
        if Out_arr[u]==[]:
            Out_arr.pop(u)
    # Готовый массив
    return Out_arr
def BFS_Krec(arr,qer, viset):
    if qer == []:
        return False
    s = qer.pop(0)
    if arr[s] not in viset:
        viset.append(arr[s])
        for i in range(len(arr)):
            if int(arr[s][i]) > 0:
                if arr[i] not in viset:
                    if i not in qer:
                        qer.append(i)
    BFS_Krec(arr, qer, viset)

def alg_Fleri(arr,s):
    end_arr = []
    # Начальная точка 0
    i_f = 0
    flag = True
    while flag == True:
        flag = False
        # ToDo Правильно выбирать новые вершины
        for i in range(len(arr)):
            if int(arr[i_f][i]) != 0:
                # Проверяем не является ли ребро мостом
                d_arr = arr
                d_arr[i_f][i] = 0
                d_arr[i][i_f] = 0
                # Взято из лаб работы 3: Проверка на кол-во компонентов связанности
                op_arr = BFS_Svaz(s)
                if len(op_arr) == 1:
                    arr = d_arr
                    end_arr.append([i_f,i])
                    i_f = i
                    flag = True
                    break
    return end_arr


s = 'input'

print(alg_Fleri(Graf_go(s),s))



