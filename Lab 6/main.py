

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
            if int(arr[i][j]) >= 1:
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
'''В начале текущее множество рёбер устанавливается пустым. Затем, пока это возможно, проводится следующая операция: 
из всех рёбер, добавление которых к уже имеющемуся множеству не вызовет появление в нём цикла, выбирается ребро 
минимального веса и добавляется к уже имеющемуся множеству. Когда таких рёбер больше нет, алгоритм завершён. Подграф 
данного графа, содержащий все его вершины и найденное множество рёбер, является его остовным деревом минимального веса. 
Подробное описание алгоритма можно найти в литературе[2].'''
def Kruskal_alg(arr):
    #Сортировка по длинне
    for i in range(len(arr)):
        for j in  range(len(arr)):
            if int(arr[i][2])<int(arr[j][2]):
                arr[i],arr[j] = arr[j],arr[i]
    print(arr)
    end_arr = [arr[0]] # Конечный массив связей
    available = [[int(arr[0][0]),int(arr[0][1])]] # Массив массивов каждый из которых является компонентой связанности
    # проверка на зацикливание дерева
    # flag = 0 - не один из узлов ещё не рассматривался
    # flag = -1 - оба узла рассматривались в одной компоненте
    # flag = 1 - один узел рассматривался
    # flag = 2 - оба узла рассматривались в разных компонентах
    for i in range(1,len(arr)):
        flag = 0
        for j in range(len(available)):
            if int(arr[i][0]) in available[j]:
                flag = 1
                if int(arr[i][1]) in available[j]:
                    flag = -1
                    break
                else:
                    for k in range(len(available)):
                        if int(arr[i][1]) in available[k]:
                            available[j] = available[j] + available[k] #Обьединение компонент связанности
                            available.pop(k)
                            flag = 2
                            end_arr.append(arr[i])
                            break
                    if flag != 2:
                        available[j].append(int(arr[i][1]))
                        end_arr.append(arr[i])
                    break
            elif int(arr[i][1]) in available[j]:
                flag = 1
                if int(arr[i][0]) in available[j]:
                    flag = -1
                    break
                else:
                    for k in range(len(available)):
                        if int(arr[i][0]) in available[k]:
                            available[j] = available[j] + available[k] #Обьединение компонент связанности
                            available.pop(k)
                            end_arr.append(arr[i])
                            flag = 2
                            break
                    if flag != 2:
                        available[j].append(int(arr[i][0]))
                        end_arr.append(arr[i])
                    break
        #print(flag)
        if flag == 0:
            available.append([int(arr[i][0]),int(arr[i][1])])
            end_arr.append(arr[i])

    print(available)

    return  end_arr
'''На вход алгоритма подаётся связный неориентированный граф. Для каждого ребра задаётся его стоимость.
Сначала берётся произвольная вершина и находится ребро, инцидентное данной вершине и обладающее наименьшей стоимостью. 
Найденное ребро и соединяемые им две вершины образуют дерево. Затем, рассматриваются рёбра графа, один конец 
которых — уже принадлежащая дереву вершина, а другой — нет; из этих рёбер выбирается ребро наименьшей стоимости. 
Выбираемое на каждом шаге ребро присоединяется к дереву. Рост дерева происходит до тех пор, пока не будут исчерпаны все вершины исходного графа.
Результатом работы алгоритма является остовное дерево минимальной стоимости.'''
def Prim_alg(arr):
    available = []
    end_arr = []

    available.append(int(0))
    for i in range(1,len(arr)):
        s_min = 1000000
        s_j = 0
        s_A = 0
        for A in available:
            for j in range(len(arr[A])):
                if int(arr[A][j]) != 0:
                    if j not in available and int(arr[A][j])<s_min:
                        s_j = j
                        s_A = int(A)
                        s_min = int(arr[A][j])
        available.append(s_j)
        end_arr.append([s_A,s_j,s_min])



    print(end_arr)



print('Минимальное оставное дерево: ',Kruskal_alg(After_read(Over_read())))
Prim_alg(Over_read())