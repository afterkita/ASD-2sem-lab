import collections
import math
# Заполнение массива по матрице путей
def Graf_go():
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
def BFS_Svaz():
    # Заполнение массива
    arr = Graf_go()
    Out_arr = []

    # Просматриваем все точки на предмет связанности
    for i in range(len(arr)):
        viset = []
        qer = []
        co = False
        # ToDo Доработать поиск
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


#Для лаб работы 2
op_arr = BFS_Svaz()
for ti in range(len(op_arr)):
    print(op_arr[ti])


