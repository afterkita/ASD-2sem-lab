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
#Сложность Беллмана Форда  O(VE)
def alg_bellman_ford(src,arr):
    #print(After_read(arr))
    # Формирование массива связей
    knot_link = After_read(arr)
    #knot_link = [[0, 1, 5],[0, 2, 4],[1, 3, 3],[2, 1, 6],[3, 2, 2]]
    dist = [float("Inf")] * len(arr) #Массив растояний
    dist[src] = 0

    for i in range(len(arr) - 1):
        for s, d, w in knot_link:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                dist[d] = dist[s] + w

    for s, d, w in knot_link:
        if dist[s] != float("Inf") and dist[s] + w < dist[d]:
            print("Не допустим отрицательный вес пути")
            return
    return dist



print(alg_Deikstr(len(Over_read())-1,Over_read()))
print(alg_bellman_ford(len(Over_read())-1,Over_read()))
#print(After_read(Over_read()))


