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
#Поиск кратчайшего пути обходом в ширину
def Whide(a,b):
    L = 0
    arr = Graf_go()
    if (a > len(arr)) or (b>len(arr)):
        return False
    elif a == b:
        return 0
    qer = []
    viset = [a]
    lengh = [-1]*len(arr)
    lengh[a] = 0
    #print(viset)
    #print(arr[a])
    for i in range(len(arr[a])):
        if int(arr[a][i]) == 1:
            qer.append(i)
            lengh[i] = lengh[a]+1
    #print(qer)
    while qer != []:
        k = qer.pop(0)
        if k == b:
            viset.append(k)
            print('Путь найден')
            print('Длинна пути: ',lengh[b])
        else:
            if k not in viset:
                viset.append(k)
                for i in range(len(arr[k])):
                    if int(arr[k][i]) == 1:
                        if i not in qer:
                            qer.append(i)
                            if i not in viset:
                                lengh[i] = lengh[k] + 1
    if lengh[b] == -1:
        print('Между узлами нет связи')

#Для лаб работы 2
a = int(input('Введите номер первого узла: '))
b = int(input('Введите номер второго узла: '))
Whide(a,b)

